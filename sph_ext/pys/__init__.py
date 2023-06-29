from typing import Any

import json
from pathlib import Path

import yaml
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

logger = getLogger(__name__)

__version__ = "2023.06.1"

# PYSCRIPT_VERSION = "2023.05.1"

PYSCRIPT_VERSION: str = None

class PyConfig(SphinxDirective):

    has_content = True

    print("PyConfig #################################")
    # Must override run() is subclass.
    # metadata = app.env.metadata[pagename]
    def run(self):

        print("PyConfig content #################", self.content)
        if self.content:
            try:
                yml_content = "\n".join(self.content)
                py_config = yaml.safe_load(yml_content)
            except Exception as e:
                logger.error(f'py-config contents is not like YAML \n {e}')
        else:
            py_config = {}

        self.env.metadata[self.env.docname]["py-config"] = json.dumps(py_config)
        logger.debug(f'################# metadata {self.env.metadata}')

        data_str = json.dumps(py_config, indent=2)

        # return []
        return [nodes.raw(
                    "",
                    f'<py-config type="json">\n{data_str}\n</py-config>\n',
                    format="html",
                )]
    
class PyRepl(SphinxDirective):

    has_content = True
    option_spec = {
        "auto-generate": directives.unchanged,
        "output": directives.unchanged,
        "src": directives.path,
    }

    def run(self):
        print("PyRepl #################################")
        attrs: str = ""
        code: str = ""

        for key, value in self.options.items():
            attrs += f' {key}="{value}"'

        if self.content:
            code = "\n".join(self.content)

        py_repl = f'''
            <py-repl {attrs}>
            {code}
            </py-repl>
        '''
        # logger.info(py_repl)
        return [nodes.raw("", py_repl, format="html")]

class PyScript(SphinxDirective):

    has_content = True
    option_spec = {
        "file": directives.path,
        "output": directives.unchanged
    }

    def run(self):

        if "file" in self.options:
            path = Path(self.env.relfn2path(self.options["file"])[1])
            try:
                code = path.read_text(encoding="utf8")
            except Exception as exc:
                raise self.error(f"Could not read file: {exc}")
            self.env.note_dependency(path)
        elif self.content:
            code = "\n".join(self.content)
        else:
            raise self.error("Must provide either content or the 'file' option")
        return [nodes.raw("", f"<py-script>\n{code}\n</py-script>\n", format="html")]
    
class PyTerminal(SphinxDirective):

    option_spec = {
        "auto": directives.flag,
        "false": directives.flag
    }

    def run(self):
        attrs: str = ""

        for key, _ in self.options.items():
            attrs += f' {key}'

        py_terminal = f'''
            <py-terminal {attrs}></py-terminal>
        '''

        return [nodes.raw("", py_terminal, format="html")]

def _add_pyscripts(app: Sphinx, pagename: str, templatename: str, context, doctree: nodes.document):

    metadata = app.env.metadata[pagename]
    if "py-config" in metadata:
        print(metadata)
        app.add_js_file(app.config.pys_js, loading_method="defer")
        app.add_css_file(app.config.pys_css)

def setup(app: Sphinx) -> dict[str, Any]:

    if PYSCRIPT_VERSION is None:
        PYSCRIPT_JS_URL = f"https://pyscript.net/latest/pyscript.js"
        PYSCRIPT_CSS_URL = f"https://pyscript.net/latest/pyscript.css"
    else:
        PYSCRIPT_JS_URL = f"https://pyscript.net/releases/{PYSCRIPT_VERSION}/pyscript.js"
        PYSCRIPT_CSS_URL = f"https://pyscript.net/releases/{PYSCRIPT_VERSION}/pyscript.css"

    app.add_config_value("pys_js", PYSCRIPT_JS_URL, "env")
    app.add_config_value("pys_css", PYSCRIPT_CSS_URL, "env")

    app.add_directive("py-config", PyConfig)
    app.add_directive("py-script", PyScript)
    app.add_directive("py-repl", PyRepl)
    app.add_directive("py-terminal", PyTerminal)

    app.connect("html-page-context", _add_pyscripts)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
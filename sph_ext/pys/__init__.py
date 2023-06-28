import json
from pathlib import Path

import yaml
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger

__version__ = "2023.06.1"
PYSCRIPT_VERSION = "2023.05.1"

LOGGER = getLogger(__name__)

def setup(app: Sphinx):
    '''sphinx config setup'''
    PYSCRIPT_JS_URL = f"https://pyscript.net/releases/{PYSCRIPT_VERSION}/pyscript.js"
    PYSCRIPT_CSS_URL = f"https://pyscript.net/releases/{PYSCRIPT_VERSION}/pyscript.css"

    app.add_config_value(
        "pys_js", PYSCRIPT_JS_URL, "env"
    )
    app.add_config_value(
        "pys_css", PYSCRIPT_CSS_URL, "env"
    )

    '''register directive for pyscript elements'''
    app.add_directive("py-config", PyConfig)
    app.add_directive("py-script", PyScript)
    app.add_directive("py-repl", PyRepl)
    app.add_directive("py-terminal", PyTerminal)

    '''define callback function'''
    app.connect("doctree-read", doctree_read)
    app.connect("html-page-context", add_pyscripts)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


class PyConfig(SphinxDirective):

    # this enables content in the directive
    has_content = True

    # Must override run() is subclass.
    def run(self):
        """Parse the config"""
        if self.content:
            try:
                temp = "\n".join(self.content)
                config = yaml.safe_load("\n".join(self.content))
            except Exception:
                raise self.error("Could not read config as YAML")
        else:
            config = {}

        self.env.metadata[self.env.docname]["py-config"] = json.dumps(config)
        LOGGER.info(f'PyConfig {self.content}')
        LOGGER.info(f'PyConfig \n{temp}')
        LOGGER.info(f'PyConfig {self.env.docname}')
        LOGGER.info(f'PyConfig {self.env.metadata}')

        return []

class PyScript(SphinxDirective):

    has_content = True
    option_spec = {
        "file": directives.path,
    }

    def run(self):
        """Add the py-script tag"""
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
    
class PyRepl(SphinxDirective):

    has_content = True
    option_spec = {
        "auto-generate": directives.flag,
        "output": directives.unchanged,
        "src": directives.path,
    }

    def run(self):
        """Add the py-repl tag"""
        attrs = ""
        code = ""
        if "auto-generate" in self.options:
            attrs += ' auto-generate="true"'
        if "output" in self.options:
            attrs += f' output="{self.options["output"]}"'
        if "src" in self.options:
            attrs += f' src="{self.options["src"]}"'
        if self.content:
            code = "\n".join(self.content)

        LOGGER.info(f'self.options \n{self.options}')
        '''raw(Special, Inline, PreBibliographic, FixedTextElement)'''
        return [nodes.raw("", f"<py-repl{attrs}>\n{code}\n</py-repl>\n", format="html")]

class PyTerminal(SphinxDirective):

    """Add a py-terminal tag"""

    option_spec = {
        "auto": directives.flag,
    }

    def run(self):
        """Add the py-terminal tag"""
        attrs = ""
        if "auto" in self.options:
            attrs += " auto"
        return [nodes.raw("", f"<py-terminal{attrs}></py-terminal>\n", format="html")]

def add_pyscripts(
    app: Sphinx, pagename: str, templatename: str, context, doctree: nodes.document
):
    """Add extra variables to the HTML template context."""
    if doctree and "pyscript" in doctree:
        app.add_js_file(app.config.pys_js, loading_method="defer")
        app.add_css_file(app.config.pys_css)

def doctree_read(app: Sphinx, doctree: nodes.document):
    """Setup the doctree."""
    metadata = app.env.metadata[app.env.docname]
    if "py-config" in metadata:
        try:
            data = json.loads(metadata["py-config"])
            assert isinstance(data, dict), "must be a dictionary"
        except Exception as exc:
            LOGGER.warning(
                f"Could not parse pyscript config: {exc}", location=(app.env.docname, 0)
            )
        else:
            doctree["pyscript"] = True
            data_str = json.dumps(data, indent=2)
            doctree.append(
                nodes.raw(
                    "",
                    f'<py-config type="json">\n{data_str}\n</py-config>\n',
                    format="html",
                )
            )

if __name__ == '__main__':
    sph = Sphinx('./docs', './docs', './docs/_build', './', 'html')
    setup(sph)
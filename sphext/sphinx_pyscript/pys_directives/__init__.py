from pathlib import Path
from sphinx.directives import SphinxDirective
from docutils.parsers.rst import directives
from docutils import nodes
from sphinx.util.logging import getLogger
import yaml
import json

logger = getLogger(__name__)

class PyConfig(SphinxDirective):

    has_content = True

    def run(self):

        if self.content:
            data = "\n".join(self.content)
            data = json.dumps(yaml.safe_load(data), indent=2)

            return [nodes.raw("", f'<py-config type="json">\n{data}\n</py-config>\n', format="html")]

class PyRepl(SphinxDirective):

    has_content = True
    option_spec = {
        "auto-generate": directives.unchanged,
        "output": directives.unchanged,
        "src": directives.path,
    }

    def run(self):
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
        return [nodes.raw("", py_repl, format="html")]

class PyScript(SphinxDirective):

    has_content = True
    option_spec = {
        "file": directives.path,
        "output": directives.unchanged
    }

    def run(self):

        if "file" in self.options:
            path = self.env.relfn2path(self.options['file'])[1]
            try:

                with open(path, 'r') as f:
                    code = f.read()
                self.env.note_dependency(path)

            except (FileNotFoundError, Exception) as err:
                logger.warn('reading error: %s, %s', path, err)
                return []

        elif self.content:
            code = "\n".join(self.content)
        else:
            raise logger.error("Must provide either content or the 'file' option")
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

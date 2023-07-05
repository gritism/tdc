from pathlib import Path
from typing import Any
import json

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.logging import getLogger
from sphinx.util.console import bold

import click 

logger = getLogger(__name__)

__version__ = "2023.06.1"

def _add_config(app: Sphinx) -> None:

    # PYSCRIPT_VERSION = "2023.05.1"
    PYSCRIPT_VERSION: str = None

    if PYSCRIPT_VERSION is None:
        PYSCRIPT_JS_URL = f"https://pyscript.net/latest/pyscript.js"
        PYSCRIPT_CSS_URL = f"https://pyscript.net/latest/pyscript.css"
    else:
        PYSCRIPT_JS_URL = f"https://pyscript.net/releases/{PYSCRIPT_VERSION}/pyscript.js"
        PYSCRIPT_CSS_URL = f"https://pyscript.net/releases/{PYSCRIPT_VERSION}/pyscript.css"

    config_list = ['pys_js', 'pys_css']

    app.add_config_value("pys_js", PYSCRIPT_JS_URL, "env")
    app.add_config_value("pys_css", PYSCRIPT_CSS_URL, "env")

    temp_config_list: list[str] = []

    for v in config_list:
        if v in app.config.values:
            temp_config_list.append(v)

    click.secho(f"[pyscript] 2. config registered: {temp_config_list}", bold=True, fg="green")

def _add_directive(app: Sphinx) -> None:

    from sphinx_pyscript.pys_directives import (
        PyConfig,
        PyRepl,
        PyScript,
        PyTerminal
    )

    d: dict[str, directives] = {
        'py-config': PyConfig,
        'py-script': PyScript,
        'py-repl': PyRepl,
        'py-terminal': PyTerminal
    }

    for k, v in d.items():
        app.add_directive(k, v)

    temp_list: list[str] = []

    for k in d:
        temp_list.append(directives._directives[k])

    click.secho(f"[pyscript] 3. directive registered: {temp_list}", bold=True, fg="green")

def _source_read(app: Sphinx, docname, source) -> None:

    if "py-config" in source[0]:
        click.secho(f"[pyscript] 4 source read -> filenm: {docname}, source: {str(source)[:30]}", bold=True, fg="green")

# delete
def _doc_read(app: Sphinx, doctree: nodes.document) -> None:

    metadata = app.env.metadata[app.env.docname]

    # click.secho(f"doctree: {doctree.children}", bold=True, fg="blue")
    # for k in metadata:
        # if k == "py-config":
    print(doctree[0][:100])

    print(list(filter(lambda x: 'py-config' in x, metadata)))
    print('py-config' in str(doctree))
    if ('py-config' in str(doctree)):
        app.add_js_file(app.config.pys_js, loading_method="defer")
        app.add_css_file(app.config.pys_css)
        click.secho(f"[pyscript] 5 build html -> filenm: {app.env.docname}, source: {str(doctree)[:30]}", bold=True, fg="green")
    elif ('py-config' in list(filter(lambda x: 'py-config' in x, metadata))):
        data = json.loads(metadata["py-config"])
        data = json.dumps(data, indent=2)

        doctree.append(
            nodes.raw(
                    "",
                    f'<py-config type="json">\n{data}\n</py-config>\n',
                    format="html",
                )
            )
    
        # app.add_js_file(app.config.pys_js, loading_method="defer")
        # app.add_css_file(app.config.pys_css)

        click.secho(f"[pyscript] 5 build html -> filenm: {app.env.docname}, source: {str(doctree)[:30]}", bold=True, fg="green")

def _page_context(app: Sphinx, pagename: str, templatename: str, context: dict, doctree: nodes.document) -> None:

    metadata = app.env.metadata[pagename]

    if ('py-config' in str(doctree)):
        app.add_js_file(app.config.pys_js, loading_method="defer")
        app.add_css_file(app.config.pys_css)
        click.secho(f"[pyscript] 5 build html -> filenm: {pagename}, source: {str(doctree)[:30]}", bold=True, fg="green")
        
    elif ('py-config' in list(filter(lambda x: 'py-config' in x, metadata))):
        data = json.loads(metadata["py-config"])
        data = json.dumps(data, indent=2)

        doctree.append(
            nodes.raw(
                    "",
                    f'<py-config type="json">\n{data}\n</py-config>\n',
                    format="html",
                )
            )
    
        app.add_js_file(app.config.pys_js, loading_method="defer")
        app.add_css_file(app.config.pys_css)

        click.secho(f"[pyscript] 5 build html -> filenm: {pagename}, source: {str(doctree)[:30]}", bold=True, fg="green")

def _add_connect(app: Sphinx) -> None:

    app.connect("source-read", _source_read)
    # app.connect("doctree-read", _doc_read)
    app.connect("html-page-context", _page_context)

def setup(app: Sphinx) -> dict[str, Any]:

    # 1. load extension
    click.secho(f"[pyscript] 1. load extension {app.config.extensions}", bold=True, fg="green")

    # 2. pyscript config
    _add_config(app)

    # 3. add directive
    _add_directive(app)

    # 4. build - read source and generate output
    _add_connect(app)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
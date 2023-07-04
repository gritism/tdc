from pathlib import Path
from typing import Any
import json

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.logging import getLogger
from sphinx.util.console import bold

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

    for inx in config_list:
        if inx in app.config.values:
            temp_config_list.append(app.config.values[inx])

    logger.info(bold("[pyscript] 2. add config value: %s"), temp_config_list)

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

    logger.info(bold("[pyscript] 3. add directive %s"), temp_list)

def _source_read(app: Sphinx, docname, source) -> None:

    if "py-config" in source[0]:
        logger.info(bold("[pyscript] 4 source read -> filenm: %s, source: %s"), docname, str(source)[:30])

def _doc_read(app: Sphinx, doctree: nodes.document) -> None:

    metadata = app.env.metadata[app.env.docname]

    for k in metadata:
        if k == "py-config":
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

            logger.info(bold("[pyscript] 5 build html -> filenm: %s, output: %s"), app.env.docname, str(doctree)[:30])

def _add_connect(app: Sphinx) -> None:

    app.connect("source-read", _source_read)
    app.connect("doctree-read", _doc_read)

def setup(app: Sphinx) -> dict[str, Any]:

    # 1. load extension
    logger.info(bold("[pyscript] 1. load extension %s"), app.config.extensions)

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
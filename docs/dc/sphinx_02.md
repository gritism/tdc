---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# autodoc

+++

```{note}
For Sphinx (actually, the Python interpreter that executes Sphinx) to find your module, it must be importable. That means that the module or the package must be in one of the directories on sys.path – adapt your sys.path in the configuration file accordingly.
```
```{warning}
autodoc imports the modules to be documented. If any modules have side effects on import, these will be executed by autodoc when sphinx-build is run.

If you document scripts (as opposed to library modules), make sure their main routine is protected by a if __name__ == '__main__' condition.
```

+++

## environment

```{code-cell} ipython3
%cd ../../../sph
```

## configure

### 1. conf.py 수정

+++

* autodoc extension 추가
```{code-block}
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']
```

+++

* code 경로 추가 (아래는 sphinx library)
```{code-block}
import os
import sys
sys.path.insert(0, os.path.abspath('~/workspace/sph/.venv/lib/python3.10/site-packages/sphinx/'))
```

+++

### 2. apidoc

```{code-cell} ipython3
!pdm run sphinx-apidoc -o ./docs .venv/lib/python3.10/site-packages/sphinx
```

```{code-cell} ipython3
!tree ./docs -L 1
```

### 3. build

```{code-cell} ipython3
:tags: [hide-output]

!pdm run sphinx-build docs/ docs/_build/html
```

```{code-cell} ipython3
!tree ./docs/_build/html -L 1
```

### 4. browse

```{code-cell} ipython3
:tags: [output_scroll]

from IPython.display import display, HTML
chart = HTML('./docs/_build/html/py-modindex.html')
# or chart = charts.plot(...)
display(chart)
```

```{code-cell} ipython3

```

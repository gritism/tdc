---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# autodoc


```{note}
For Sphinx (actually, the Python interpreter that executes Sphinx) to find your module, it must be importable. That means that the module or the package must be in one of the directories on sys.path – adapt your sys.path in the configuration file accordingly.
```
```{warning}
autodoc imports the modules to be documented. If any modules have side effects on import, these will be executed by autodoc when sphinx-build is run.

If you document scripts (as opposed to library modules), make sure their main routine is protected by a if __name__ == '__main__' condition.
```



## environment

```python tags=["hide_cell"]
import os

home_dir = os.path.expanduser('~')
work_dir = f'{home_dir}/workspace/sphinx_demo'

os.chdir(work_dir)
!pwd
```

## configure

### 1. conf.py 수정


* autodoc extension 추가
```{code-block}
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']
```


* code 경로 추가 (아래는 sphinx library)
```{code-block}
import os
import sys
sys.path.insert(0, os.path.abspath('~/workspace/sph/.venv/lib/python3.10/site-packages/sphinx/'))
```


### 2. apidoc

```python
!pdm run sphinx-apidoc -o ./docs .venv/lib/python3.10/site-packages/sphinx
```

```python
!tree ./docs -L 1
```

### 3. build

```python tags=["hide-output"]
!pdm run sphinx-build docs/ docs/_build/html
```

```python
!tree ./docs/_build/html -L 1
```

### 4. browse

```python tags=["output_scroll"]
from IPython.display import display, HTML
html = HTML('./docs/_build/html/sphinx.html')
display(html)
```

```python

```

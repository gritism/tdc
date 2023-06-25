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

# sphinx


* sphinx는 document generation을 위한 라이브러이임
* document 작성을 위한 언어로 rst를 기본으로 하며(markdown도 지원)
* python docstring을 자동화하여 api document생성 지원. 
    * (공식 python document도 sphinx를 이용하여 제공하고 있음)
    


## environment 준비

```python
import os

home_dir = os.path.expanduser('~')
# work_dir = f'{home_dir}/sphinx_demo'
print(home_dir)
```

```python
!pip install pdm
```

```python
work_dir = f'{home_dir}/sphinx_demo'
print(work_dir)
```

```python
if not os.path.isdir(work_dir):
    os.mkdir(work_dir)
# else:
#     os.system(f'rm -rf '+work_dir)
#     os.mkdir(work_dir)
    
os.chdir(work_dir)
```

```python
!pwd
```

## install

```python
!pdm init -n
```

```python
!pdm venv create -w virtualenv
```

```python
!pdm use --venv in-project
```

```python tags=["hide-output"]
!pdm add sphinx
```

```python
!pdm list --graph
```

## create book

```python
!pdm run sphinx-quickstart docs -q -p sph_test -a YB
```

```python
!tree .
```

## build

```python
!pdm run sphinx-build docs/ docs/_build/html
```

## browse

```python
from IPython.display import display, HTML
chart = HTML('./docs/_build/html/index.html')
# or chart = charts.plot(...)
display(chart)
```

```python

```

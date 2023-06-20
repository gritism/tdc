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


sphinx는 document generation을 위한 라이브러이임
document 작성을 위한 언어로 rst를 기본으로 하며(markdown도 지원), python docstring을 자동화하여 api document생성도 지원함. (공식 python document도 sphinx를 이용하여 제공하고 있음)


## environment 준비

```python
import os
```

```python
os.chdir("../../../") #working directory 변경
```

```python
os.getcwd()
```

```python
work_dir = "sph"
if not os.path.isdir(f'./'+work_dir):
    os.mkdir(work_dir)

os.chdir(f'./'+work_dir)
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

```python
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

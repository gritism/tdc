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

# sphinx

+++

sphinx는 document generation을 위한 라이브러이임
document 작성을 위한 언어로 rst를 기본으로 하며(markdown도 지원), python docstring을 자동화하여 api document생성도 지원함. (공식 python document도 sphinx를 이용하여 제공하고 있음)

+++

## environment 준비

```{code-cell} ipython3
import os
```

```{code-cell} ipython3
os.chdir("../../../") #working directory 변경
```

```{code-cell} ipython3
work_dir = "sph"
if not os.path.isdir(f'./'+work_dir):
    os.mkdir(work_dir)
else:
    os.system(f'rm -rf '+work_dir)
    os.mkdir(work_dir)
    
os.chdir(f'./'+work_dir)
```

## install

```{code-cell} ipython3
!pdm init -n
```

```{code-cell} ipython3
!pdm venv create -w virtualenv
```

```{code-cell} ipython3
!pdm use --venv in-project
```

```{code-cell} ipython3
:tags: [hide-output]

!pdm add sphinx
```

```{code-cell} ipython3
!pdm list --graph
```

## create book

```{code-cell} ipython3
!pdm run sphinx-quickstart docs -q -p sph_test -a YB
```

```{code-cell} ipython3
!tree .
```

## build

```{code-cell} ipython3
!pdm run sphinx-build docs/ docs/_build/html
```

## browse

```{code-cell} ipython3
from IPython.display import display, HTML
chart = HTML('./docs/_build/html/index.html')
# or chart = charts.plot(...)
display(chart)
```

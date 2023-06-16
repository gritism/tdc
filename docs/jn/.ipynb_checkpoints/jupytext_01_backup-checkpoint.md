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

(file-types:pandas_01)=

# jupytext test

+++

## install

```{code-cell} ipython3
#!pdm add jupytext
```

```{code-cell} ipython3
!pdm show jupytext
```

## config

```{warning}
    jupytext는 notebook > 7 버전과 아직 호환되지 않음. (23.6월 기준) notebook <= 6 이하 버전 설치해야 함
```

```{code-cell} ipython3
from jupytext.config import global_jupytext_configuration_directories
list(global_jupytext_configuration_directories())
```

```{code-cell} ipython3
from jupytext.config import find_jupytext_configuration_file
find_jupytext_configuration_file('.')
```

```{code-cell} ipython3
print('final success')
```

```{code-cell} ipython3

```

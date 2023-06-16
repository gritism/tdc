---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Technical Document Center

- python 관련 기술 문서 정리를 위한 공간
- 데이터 분석/시각화, 머신러닝, 딥러닝 등 관심 영역에 대한 내용을 정리할 예정

-------------

<!-- ---
title: Books with Jupyter
--- -->

{bdg-primary}`A` Information
* Octicon Icons: {octicon}`beaker;1em;sd-text-info`
* {octicon}`question;1em;sd-text-info` Ask and answer questions
-----

{bdg-primary}`B` change  
```{code-cell} ipython3
:tags: ['remove-input']

from myst_nb import glue
import pandas as pd
df = pd.read_pickle('./history/history.pickle')
df = df.sort_values(['date'], ascending=False)
df.head()
```
-------

{bdg-primary}`C` reference site
```{list-table} 
:header-rows: 1
* - ref
  - 설명
* - [{bdg-info-line}`sphinx-design`](https://sphinx-design.readthedocs.io/en/rtd-theme/)
  - sphinx extension으로 grid, tab, icon 등 desing 컴포넌트 제공
* - [{bdg-info-line}`MyST cheat sheet`](https://jupyterbook.org/en/stable/reference/cheatsheet.html)
  - MyST markdown reference site  
```

-------


::::{grid} 3

:::{grid-item-card} {bdg-primary}`A` to-do
:::

:::{grid-item-card} {bdg-primary}`B` change
:::

:::{grid-item-card} {bdg-primary}`C` ref
:::
::::

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
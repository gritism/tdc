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

-------------

<!-- ---
title: Books with Jupyter
--- -->

{bdg-primary}`A` Information
* {octicon}`report;1em;sd-text-info` python 관련 기술 문서 정리를 위한 공간 테스트 3(github action)
* {octicon}`report;1em;sd-text-info` 관심분야: 데이터 분석/시각화, 머신러닝, 딥러닝 등 

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
* - [{bdg-info-line}`jupyter book`](https://jupyterbook.org/en/stable/reference/cheatsheet.html)
  - jupyter book site: executable book 개발을 위한 라이브러리 제공   
* - [{bdg-info-line}`MyST`](https://mystmd.org/guide/quickstart)
  - MyST markdown reference site  
```

-------


::::{grid} 3

:::{grid-item-card} to-do
- [ ] thebe
- [ ] autodoc
- [ ] LaTex
:::

:::{grid-item-card} change
:::

:::{grid-item-card} ref
:::
::::

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
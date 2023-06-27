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

::::{grid} 1 1 1 1

:::{grid-item}
{bdg-primary}`1` Overview
* {octicon}`report;1em;sd-text-info` python 관련 기술 문서 정리를 위한 공간
* {octicon}`report;1em;sd-text-info` 관심분야: 데이터 분석/시각화, 머신러닝, 딥러닝, 문서자동화 등 
:::

:::{grid-item}
{bdg-primary}`2` to-do
- [x] [mermaid](`./dc/mermaid.md`)
- [ ] thebe
- [ ] autodoc
- [ ] ablog for sphinx
- [ ] stock analysis (bokeh application using public data open api)
:::

:::{grid-item}
{bdg-primary}`3` change  
```{include} ./chg_summary.md
```  
:::

:::{grid-item}
{bdg-primary}`4` reference site
```{list-table} 
:header-rows: 1
* - ref
  - 설명
* - [{bdg-success}`sphinx-design`](https://sphinx-design.readthedocs.io/en/rtd-theme/)
  - sphinx extension으로 grid, tab, icon 등 desing 컴포넌트 제공
* - [{bdg-success}`jupyter book`](https://jupyterbook.org/en/stable/reference/cheatsheet.html)
  - jupyter book site: executable book 개발을 위한 라이브러리 제공   
* - [{bdg-success}`MyST`](https://mystmd.org/guide/quickstart)
  - MyST markdown reference site  
* - [{bdg-success}`Shibuya`](https://shibuya.lepture.com/)
  - beautiful sphinx theme, Highly customization  
```
:::
::::

```{only} html
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2561065.svg)](https://doi.org/10.5281/zenodo.2561065)
```
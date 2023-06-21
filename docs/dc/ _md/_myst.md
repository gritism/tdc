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

# myst


* MyST is an extension of [**CommonMark Markdown**](https://commonmark.org/)
* MyST can integrate with **Docutils and Sphinx.**


::::{grid} 1 1 1 1

:::{grid-item}
```{list-table} sphinx extension
* - extension
  - description
* - sphinx-design
  - beautiful, responsive web components to your documentation
* - sphinx-copybutton
  - a copy button to your code blocks
* - sphinx-rediraffe
  - redirects to your documentation
* - sphinx-opengraph
  - OpenGraph metadata to your documentation
* - sphinx-pyscript
  - execute python code in your documentation
* - sphinx-tippy
  - tooltips to your documentation
* - sphinx-autodoc2
  - generate documentation from docstrings
* - sphinx-togglebutton
  - collapsible content to your documentation
* - sphinx-mermaid
  - generate Mermaid diagrams
```
:::
::::


## 1. install

```python
import os

home_dir = os.path.expanduser('~')
work_dir = f'{home_dir}/workspace/tdc'

os.chdir(work_dir)
!pwd
```

```python tags=["hide-output"]
!pdm add myst-parser
```

```python
!pdm show myst-parser
```

## 2. markdown syntax


### 2.1 example


**markdown example**
```
    ### header 3
    * unordered list
        * unordered list
    ```{admonition} This is custom title
    :class: dropdown
    this is a message
    ```
    badge {bdg-primary}`badge`
```


**result**

> ### header 3
> * unordered list
>    * unordered list
> ```{admonition} This is custom title
> :class: dropdown
> this is a message
> ```
> badge {bdg-primary}`badge`



### 2.2 guide

* [주요 가이드](./markdown.md)


## 3. use MyST in sphinx


### 3.1 configure (conf.py in sphinx)

* sphinx가 설치되어 있지 않으면 sphinx 설치
* sphinx 설정 파일 `conf.py`에 myst extension 추가


`conf.py` 파일 수정
> ```
> extensions = ['myst_parser']
> ```

```python

```

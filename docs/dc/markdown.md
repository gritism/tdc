(myst_cheatsheet)=
# myst-detail
※ jupyter book의 ['MyST syntax cheat sheet'](https://jupyterbook.org/en/stable/reference/cheatsheet.html#) 참조하여 추가 정리

```{note}
:class: dropdown

/
```

## Header
::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```{code-block}
  # Heading level 1
  ## Heading level 2
  ### Heading level 3
  #### Heading level 4
  ##### Heading level 5
  ###### Heading level 6
  ```
:::
:::{grid-item-card}
:shadow: none
result
^^^
```{rubric} Heading level 3
:::
::::

## Quote

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    > This is a quote
  ```
:::
:::{grid-item-card} result
:shadow: none
  > This is a quote
:::
::::

## List

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    1. First item
    2. Second item
        1. First sub-item
  ```
:::
:::{grid-item-card} result
:shadow: none
  1. First item
  2. Second item
     1. First sub-item
:::
::::

## Link

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    [Jupyter Book](https://jupyterbook.org)
  ```
:::
:::{grid-item-card} result
:shadow: none
  [Jupyter Book](https://jupyterbook.org)
:::
::::

## Table

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ````md
    ```{list-table} This table title
    :header-rows: 1
    :name: example-table

    * - Training
      - Validation
    * - 0
      - 5
    * - 13720
      - 2744
    ```
  ````
:::
:::{grid-item-card} result
:shadow: none
  ```{list-table} This table title
    :header-rows: 1
    :name: example-table

    * - Training
      - Validation
    * - 0
      - 5
    * - 13720
      - 2744
  ```
:::
::::

## Admotion

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
syntax
^^^
````md
  ```{admonition} This is a title
    An example of an admonition with a title.
  ```
````
:::
:::{grid-item-card}
result
^^^
`````{tab-set}

````{tab-item} Note
```{note}
This is an note admonition
```
````

````{tab-item} Important
```{important}
This is an important admonition
```
````

````{tab-item} Hint
```{hint}
This is an hint admonition
```
````

````{tab-item} See Also
```{seealso}
This is an seealso admonition
```
````

````{tab-item} Tip
```{tip}
This is an tip admonition
```
````

````{tab-item} Attention
```{attention}
This is an attention admonition
```
````

````{tab-item} Caution
```{caution}
This is an caution admonition
```
````

````{tab-item} Warning
```{warning}
This is an warning admonition
```
````

````{tab-item} Danger
```{danger}
This is an danger admonition
```
````

````{tab-item} Error
```{error}
This is an error admonition
```
````
`````
:::
::::

## Figure

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    ```{image} ../images/C-3PO_droid.png
    :height: 150px
    :name: image-example
    ```
  ```
:::
:::{grid-item-card} result
:shadow: none
  ```{image} ../img/tdc_logo_3.png
    :height: 100px
    :name: image-example
  ```
:::
::::

## to-do list

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    ```
    - [ ] Mercury
    - [ ] Venus
    - [ ] Earth
    - [ ] Mars
    ```
  ```
:::
:::{grid-item-card} result
:shadow: none
  - [x] Mercury
  - [ ] Venus
  - [ ] Earth
  - [ ] Mars
:::
::::

## emoji (octicon)

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    ```
    [sphinx style]
    - {octicon}`smiley;1em;sd-text-info`

    [github style]
    - |:smiley:|
    ```
  ```
:::
:::{grid-item-card} result
:shadow: none
```{list-table} 
:header-rows: 0
* - {octicon}`smiley;1em;sd-text-info`
  - {octicon}`thumbsup;1em;sd-text-info`
  - {octicon}`workflow;1em;sd-text-info`
  - {octicon}`tag;1em;sd-text-info`
  - {octicon}`arrow-right;1em;sd-text-info`
* - smiley
  - thumbsup
  - workflow
  - tag
  - arrow-right
```
  ```{button-link} https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#octicon-icons
  :color: primary
  :outline:
  octicon 바로가기
  ```
:::
::::

## button

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    ```{button-link} https://example.com
    :color: primary
    :outline:
    button
    ```
  ```
:::
:::{grid-item-card} result
:shadow: none
  ```{button-link} https://sphinx-design.readthedocs.io/en/rtd-theme/badges_buttons.html#buttons
  :color: primary
  :outline:
  button
  ```
:::
::::

## tab

::::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    ::::{tab-set}

    :::{tab-item} Label1
    Content 1
    :::

    :::{tab-item} Label2
    Content 2
    :::

    ::::
  ```
:::::
:::::{grid-item-card} result
:shadow: none

````{tab-set}

```{tab-item} Label1
Content 1
```

```{tab-item} Label2
Content 2
```
````
:::::
::::::

## Math

::::{grid} 1 1 1 1
:gutter: 3

  :::{grid-item-card}
  :shadow: none
  syntax
  ^^^
    ```md
      This is an example of a
      math block

      $$
      z=\sqrt{x^2+y^2}
      $$
    ```
  :::
  :::{grid-item-card} result
  :shadow: none
    This is an example of a
    math block

    $$
    z=\sqrt{x^2+y^2}
    $$
  :::
::::

## block code

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card}
:shadow: none
syntax
^^^
  ```md
    Wrap in-line code blocks in backticks: `boolean example = true;`.
  ```
:::
:::{grid-item-card} result
:shadow: none
  ```python
    note = "Python syntax highlighting"
    print(node)
  ```
:::
::::

## grid

::::{grid} 1 1 1 1
:gutter: 3

  :::{grid-item-card}
  :shadow: none
  syntax
  ^^^
    ```md
      ::::{grid} 3
      :outline:

      :::{grid-item}
      A
      :::
      :::{grid-item}
      B
      :::
      :::{grid-item}
      C
      :::
      ::::
    ```
  :::
  :::{grid-item-card}
  :shadow: none
  result
  ^^^
  ::::{grid} 3 3 3 3
  :outline:

    :::{grid-item}
    A
    :::
    :::{grid-item}
    B
    :::
    :::{grid-item}
    C
    :::
  ::::
  :::
::::
------


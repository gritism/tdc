(myst_cheatsheet)=
# markdown
※ jupyter book의 ['MyST syntax cheat sheet'](https://jupyterbook.org/en/stable/reference/cheatsheet.html#) 참조하여 추가 정리

## Header

::::{grid} 2

:::{grid-item-card} syntax
  ```md
      # Heading level 1
      ## Heading level 2
      ### Heading level 3
      #### Heading level 4
      ##### Heading level 5
      ###### Heading level 6
  ```
:::
:::{grid-item-card} result
  ### Heading level 3
:::
::::

## Quote

::::{grid} 2

:::{grid-item-card} syntax
  ```md
    > This is a quote
  ```
:::
:::{grid-item-card} result
  > This is a quote
:::
::::

## List

::::{grid} 2

:::{grid-item-card} syntax
  ```md
    1. First item
    2. Second item
        1. First sub-item
  ```
:::
:::{grid-item-card} result
  1. First item
  2. Second item
     1. First sub-item
:::
::::

## Link

::::{grid} 2

:::{grid-item-card} syntax
  ```md
    [Jupyter Book](https://jupyterbook.org)
  ```
:::
:::{grid-item-card} result
  [Jupyter Book](https://jupyterbook.org)
:::
::::

## Table

::::{grid} 2

:::{grid-item-card} syntax
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

::::{grid} 2

:::{grid-item-card} syntax
  ```md
    ```{admonition} This is a title
    An example of an admonition with a title.
    ```
  ```
:::
:::{grid-item-card} result
  ```{admonition} This is a title
    An example of an admonition with a title.
  ```
:::
::::

## Figure

::::{grid} 2

:::{grid-item-card} syntax
  ```md
    ```{image} ../images/C-3PO_droid.png
    :height: 150px
    :name: image-example
    ```
  ```
:::
:::{grid-item-card} result
  ```{image} ../tdc_logo_3.png
    :height: 90px
    :name: image-example
  ```
:::
::::

## Math

::::{grid} 2

  :::{grid-item-card} syntax
    ```md
      This is an example of a
      math block

      $$
      z=\sqrt{x^2+y^2}
      $$
    ```
  :::
  :::{grid-item-card} result
    This is an example of a
    math block

    $$
    z=\sqrt{x^2+y^2}
    $$
  :::
::::

## block code

::::{grid} 2

:::{grid-item-card} syntax
  ```md
    Wrap in-line code blocks in backticks: `boolean example = true;`.
  ```
:::
:::{grid-item-card} result
  ```python
    note = "Python syntax highlighting"
    print(node)
  ```
:::
::::

## grid

::::{grid} 1
  :gutter: 1

  :::{grid-item-card} syntax
    ```
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
  :::{grid-item-card} result
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
  :::
::::


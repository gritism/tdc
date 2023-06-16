(myst_cheatsheet)=
# markdown
※ jupyter book의 ['MyST syntax cheat sheet'](https://jupyterbook.org/en/stable/reference/cheatsheet.html#) 참조하여 추가 정리

```{note}
:class: dropdown

/
```

## Header
::::{grid} 1 1 2 2

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
  '\### Heading level 3
:::
::::

## Quote
```{note}
:class: dropdown


```

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

::::{grid} 1 1 1 1
:gutter: 3

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

::::{grid} 1 1 1 1
:gutter: 3

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

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card} syntax
````md
  ```{admonition} This is a title
    An example of an admonition with a title.
  ```
````
:::
:::{grid-item-card} syntax
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
    :height: 100px
    :name: image-example
  ```
:::
::::

## to-do list

::::{grid} 2

:::{grid-item-card} syntax
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
  - [x] Mercury
  - [ ] Venus
  - [ ] Earth
  - [ ] Mars
:::
::::

## emoji (octicon)

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card} syntax
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

:::{grid-item-card} syntax
  ```md
    ```{button-link} https://example.com
    :color: primary
    :outline:
    button
    ```
  ```
:::
:::{grid-item-card} result
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

:::::{grid-item-card} syntax
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

::::{grid} 1 1 1 1
:gutter: 3

  :::{grid-item-card} syntax
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
  :::{grid-item-card} result
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


<!-- :::{div} sd-text-left sd-text-primary sd-fs-4 sd-font-weight-bolder  
  ## Header
::: -->


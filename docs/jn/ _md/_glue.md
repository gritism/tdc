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

<!-- #region editable=true slideshow={"slide_type": ""} -->
# glue
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
```{admonition} definition
add a key to variables in a notebook, 
then **display those variables in your book by referencing the key.**
```
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## glue function
* name: book(page) 상세서 사용되는 유니크 명칭(key)
* variable: jupyter notebook으로 생성된 객체(str, graph etc)
* display: true/false
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
from myst_nb import glue
```

```python editable=true slideshow={"slide_type": ""}
help(glue)
```
<!-- #region editable=true slideshow={"slide_type": ""} -->
## usecase
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### graph
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### 1) drawing scatter graph
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Visualize seaborn scatter chart
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="dark")

# Simulate data from a bivariate Gaussian
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(4, 4))
sns.scatterplot(x=x, y=y, s=5, color=".15")
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

glue("scatter_graph", f, display=False)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### 2) display the graph
* binding the graph(f) in in-line text(markdown)
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
::::{tab-set}
:::{tab-item} example
```
In-line text; a figure: {glue:}`scatter_graph`.
```
:::
::::
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
::::{tab-set}
:::{tab-item} result
In-line text; a figure: {glue:}`scatter_graph`
:::
::::
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### table
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### 1) dataframe
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.style.set_table_attributes('style="font-size: 10px"')

glue('df_tbl', df.head())
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### 2) display(binding) in the book
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
::::{tab-set}
:::{tab-item} example
```
```{glue:figure} df_tbl
:figwidth: 100px
:name: 'tbl:df'

titanic dataset
```
:::
::::
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
::::{tab-set}
:::{tab-item} result
```{glue:figure} df_tbl
:figwidth: 80%
:name: 'tbl:df'

titanic dataset
```
:::
::::
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}

```

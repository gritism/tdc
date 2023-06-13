.. role:: raw-html-m2r(raw)
   :format: html


seaborn
=======


* data visualization library based on **matplotlib**

install
-------


* ``pdm add seaborn (or pip install seaborn)``

Basic
-----


* import ``import seaborn as sns``
* set_theme()
  ..

     ``seaborn.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)``


* load dataset
  ..

     ``seaborn.load_dataset(name, cache=True, data_home=None, **kws)``\ :raw-html-m2r:`<br>`
     dataset name 목록: {https://github.com/mwaskom/seaborn-data}


     * tips = sns.load_dataset("tips)


* create chart

  * chart 종류

    * Relational plots (relplot, scatterplot, lineplot)
    * Distribution plots (displot, histplot, kdeplot et)
    * Categorical plots (catplot, boxplot, violinplot etc)
    * Regression plots (lmplot, regplot etc)
    * Maxtrix plots (heatmap, clustermap)
    * Multi-plot grids (jointplot, FacetGrid etc)

  * relplot  
    ..

       ``seaborn.relplot(data=None, *, x=None, y=None, hue=None, size=None, style=None, units=None, row=None, col=None, col_wrap=None, row_order=None, col_order=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=None, dashes=None, style_order=None, legend='auto', kind='scatter', height=5, aspect=1, facet_kws=None, **kwargs)``


  * example
    .. code-block::

         sns.relplot(
         data=tips,
         x="total_bill", y="tip", col="time",
         hue="smoker", style="smoker", size="size",
         )

Advanced
--------

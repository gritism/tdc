# rst
* rst: reStructuredText files
* markup language that is common in the python documentation community

```{note}
* markdown이 rst보다 문법이 심플해서 많이 사용한다고 하나,
* 현재는 markdown 문법도 복잡해져서 rst와 복잡성을 비슷해짐
* 단, markdwon 사용자들이 많고 익숙한 형태로 markdwon을 많이 사용하는 것으로 보임
``` 

## rst example
```
.. note::

   A note written in reStructuredText.

.. include:: ./include-rst.rst
```
```{eval-rst}
.. note::

   A note written in reStructuredText.

.. include:: ./include-rst.rst
```

## rst vs. markdown
* 작성 방식이 조금 다를 뿐 서로 유사 (benchmarking)
```{list-table}
* - rst
  - markdown
* - 
    ```
    .. code-block:: html
        <h1>code block example</h1>
    ```
  - 
    ```md
    ```{code-block}
        <h1>code block example</h1>
    ```
* - 
    ```
    .. image:: starts.jpg
        :width: 200px
    ```
  - 
    ```md
    ```{image}`path`
    :width: 200px
    ```
* - 
    ```
    .. note:: This is a note box

    ```
  - 
    ```md
    ```{note}
    This is a note box
    ```
```

[sphinx-rst](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

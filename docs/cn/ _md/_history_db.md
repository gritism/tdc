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

```python
import pandas as pd
import datetime
```

```python
df = pd.DataFrame(columns=['date', 'history'])
```

```python
df.loc[len(df)] = ['20230607', '최초 생성 - python 관련 기술 내용 정리 목적']
```

```python
df.head()
```

```python
df.to_pickle('./history.pickle')
```

```python
temp = pd.read_pickle('./history.pickle')
```

```python
temp.head()
```

```python

```

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

(file-types:is)=
# finance


```python vscode={"languageId": "python"}
import pandas as pd
```

```python vscode={"languageId": "python"}
#df = pd.read_csv('./data/2016_FS.txt', sep = "\t", engine='python', encoding='cp949')
```

```python vscode={"languageId": "python"}
import pymysql
from sqlalchemy import create_engine, text
# conn = pymysql.connect(host='localhost',
#                              user='admin',
#                              password='admin1234',
#                              db='STOCKDB',
#                              charset='utf8')

engine = create_engine('mysql+pymysql://admin:admin1234@localhost/STOCKDB')
connn = engine.connect()
# curs = conn.cursor()
```

```python vscode={"languageId": "python"}
# df.to_sql(name='fs1', con=engine, if_exists='append', index=False)
```

```python vscode={"languageId": "python"}
sql = "select * from pb_fs"
result = pd.read_sql(sql, engine)
# with engine.connect() as conn:
#     result = conn.execute(text(sql)).fetchall()
```

```python vscode={"languageId": "python"}
result.columns
```

```python vscode={"languageId": "python"}
result.head()
```

```python vscode={"languageId": "python"}

```

```python

```

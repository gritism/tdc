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

(file-types:jupytext_01)=

# jupytext


## why

* jupyter notebook(**.ipynb**) 파일은 버전 관리가 어려움
* **jupytext는 ipynb 파일을 .py, .md 등 plain text 형태 파일로 전환해주는 것임.**
* .py, .md 파일을 github를 통해 버전관리를 할 수 있음


## install

```python
#!pdm add jupytext
```

```python
!pdm show jupytext
```

## config

```{warning}
    jupytext는 notebook > 7 버전과 아직 호환되지 않음. (23.6월 기준) notebook <= 6 이하 버전 설치해야 함
```


1. jupytext config 파일 위치 가능한 디렉토리 목록
    * 아래 디렉토리 리스트에 jupytext config 파일 생성 가능 

```python
from jupytext.config import global_jupytext_configuration_directories
list(global_jupytext_configuration_directories())
```

2. `jupytext.yml` 파일에 아래 내용 작성  
    {octicon}`report;1em;sd-text-info` 기본적으로 jupytext는 ipynb, md 파일을 동일 디렉토리에 생성/저장
    저장 경로를 다르게 하기 위한 config 파일 구성임.
    ```
        formats: "ipynb, scripts//.md"
    ```


3. jupytext.yml 파일 인식여부 확인

```python
from jupytext.config import find_jupytext_configuration_file
find_jupytext_configuration_file('.')
```

4. jupyter notebook 실행  
{octicon}`alert-fill;1em;sd-text-info` 기존 작성된 ipynb 파일은 오류 발생하는 경우가 존재함.


## execute


1. notebook 실행 후 ipynb 파일 생성
2. pairing: `file > jupytext > Pair Notebook with Markdown` 메뉴 선택
3. save: jupytext_01.ipynb 파일 저장하면 동시에 scripts 폴더 내 `jupytext_01.md` 파일 저장

```python
!tree .
```

```python

```

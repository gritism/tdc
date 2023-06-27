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


```{admonition} Objective

* jupyter notebook(**.ipynb**) 파일은 binary로 버전 관리가 어려움.
* **jupytext는 ipynb 파일을 .py, .md 등 plain text 형태 파일로 전환해주는 것임.**
* .py, .md 파일 형태로 github를 통해 버전관리를 할 수 있음
```


## 1. install

```python tags=["hide-output"]
#!pdm add jupytext
```

```python
!pdm show jupytext
```

## 2. config


### 2.1. jupytext config 디렉토리
    * 아래 디렉토리 리스트에 jupytext config 파일 생성 가능 

```python
from jupytext.config import global_jupytext_configuration_directories
list(global_jupytext_configuration_directories())
```

### 2.2. comfig 파일 생성 

* jupytext.yml (yml파일 혁식)
    * 위치: 위 디렉토리 중 선택  
    {octicon}`report;1em;sd-text-info` 기본적으로 jupytext는 ipynb, md 파일을 동일 디렉토리에 생성/저장
    저장 경로를 다르게 하기 위한 config 파일 구성임.  
    formats: "경로/prefix/확장자, 경로/prefix/확장자"
    ```
        formats: "ipynb, _md//.md"
    ```

* pyproject.toml 파일에 기록 (pdm, poetry 등 python package 관리 툴 사용하는 경우)
    * 위치: {프로젝트 폴더}/.pyproject.toml
    * 작성
    ```
    [tool.jupytext]
    formats = "ipynb, _md/_/.md"
    ```


### 2.3. jupytext.yml 파일 인식여부 확인

```python
from jupytext.config import find_jupytext_configuration_file
find_jupytext_configuration_file('.')
```

### 2.4. jupyter notebook 실행  


## 3. execute


1. notebook 실행 후 ipynb 파일 생성
2. pairing: `file > jupytext > Pair Notebook with Markdown` 메뉴 선택
3. save: jupytext_01.ipynb 파일 저장하면 동시에 scripts 폴더 내 `jupytext_01.md` 파일 저장

```python
!tree -l
```

## bug


### 1. pairing


* paring 하는 2가지 방법
    1. jupyter notebook에서 pairing
        * notebook File > jupytext > Pair notebook with ~ 선택
    2. configuration 파일에서 설정
        * 위 config 방법으로 설정 시 notebook 에서 Pair 설정할 경우 pair 파일 중복

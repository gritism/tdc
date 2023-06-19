---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# quickstart

```{note}
1. **install**: jupyter-book library 설치
2. **create**: jupyter sample book 생성
3. **build**: html 파일 생성
4. **browse**: 웹 브라우저로 book 확인
```

```{code-cell} ipython3
%cd ../../../
%pwd
```

## 1. install

```{code-cell} ipython3
#!pdm add jupyter-book
!pdm --version
```

## 2. create

+++

* `pdm run jb create {폴더명}`
* {폴더명} 안에 관련 파일 생성됨(_config.yml, _toc.yml, intro.md 등)
  * `_config.yml`: jupyter book 환경 설정 파일
  * `_toc.yml`: 메뉴 구성 파일
  * `intro.md`: 메인화면 구성 파일

```{code-cell} ipython3
!tree ./docs -L 1 -l 
```

## 3. build

+++

* _build 폴더 내 html 파일 생성
```{tip}
* 이전 빌드되었던 내용 삭제(_build 폴더 안 내용)
  * {bdg-info}`pdm run jb clean {폴더명}` or {bdg-info}`pdm run jb build **--all** {폴더명}`
* clean하지 않을 경우 이전 내용이 캐쉬되어 정상적으로 보여지지 않는 경우 존재
```

```{code-cell} ipython3
%pwd
!pdm run jb build docs/
```

<참고: build option>

```{code-cell} ipython3
!pdm run jb build --help
```

## 4. browse

+++

- '_build/html/index.html'을 브라우저로 열면 아래 화면 실행
```{figure} ./img/jb_02.png
  :width: 80%
```
- 아래는 github pages로 호스팅

```{code-cell} ipython3
from IPython.display import IFrame
```

```{code-cell} ipython3
IFrame(src='https://yoblee.github.io/tdc', width=700, height=400)
```

```{code-cell} ipython3

```

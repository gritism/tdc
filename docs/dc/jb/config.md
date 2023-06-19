# config
* configure jupyter book

## default
* 책 제목, 저자 및 로고 설정 부분
```md
    title: My sample book
    author: The Jupyter Book Community
    logo: logo.png
```

## notebooks execution 설정
* jupyter notebook cache control
* 옵션: auto, force, cache, inline, off

## latex output file
* PDF 출력 시
```
    latex:
    latex_documents:
        targetname: book.tex
```

## sphinx configure
* jupyter book은 sphinx 엔진을 기반으로 개발되어 있으며
* sphinx 기능을 활용하기 위한 것으로 아래는 sphinx_rtd_theme을 사용하기 위한 것임
```
`pdm add sphinx-rtd-theme` 설치후 _config.yml 파일 수정
sphinx:
  config:
    html_theme: sphinx_rtd_theme
```
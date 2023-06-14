# _toc
* manage manu structure

## default
* 메뉴 구성 예시
```md
format: jb-book
root: intro
parts:
- caption: doc generator
  chapters:
  - file: doc-generator/jupyter-book
    sections:
    - file: doc-generator/jb/overview
    - url: https://jupyterbook.org/en/stable/reference/cheatsheet.html
      title: MyST syntax
```
* 설명  
    * `format:` jb-book, jb-article 2개 종류 
    * `root:` 메인 시작 화면 정의
    * `parts:` chapter의 묶음
    * `chapters:` 책의 1장, 2장 ...
    * `sections:` chapter의 sub 구분
    * `caption:` 명칭
    * `file:` markdown, rst 등 실제 문서 파일
    * `url:` 외부 사이트 문서 링크

# table of contents
* 책 목차(table of contents) 정의하는 영역
* `_toc.yml` location: {book_dir}/_toc.yml

## 1. toc(`_toc.yml`) 파일 구성
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

## 2. 항목 설명

```{list-table}
:header-rows: 1
* - 항목
  - 설명
* - {bdg-info}`format:`
  - jb-book, jb-article 2개 종류
    * jb-book(part, chapter로 구성), jb-article(only section으로만 구성)
* - {bdg-info}`root:`
  - 책의 첫번째 페이지 명칭
* - {bdg-info}`parts:`
  - 여러 chapter의 묶음 단위임. 논리적으로는 책을 구분하는 단위로 볼 수 있음. parts가 책 1권
* - {bdg-info}`chapters:`
  - 책의 chapters로 여러개로 구성 가능 (책의 1장, 2장 ...)
* - {bdg-info}`sections:`
  - chapter 내 내용을 sections으로 구분
* - {bdg-info}`caption:`
  -   
    * parts는 별도 .md 파일이 존재하지 않기 때문에 `caption`으로 명칭 부여
    * parts의 caption은 좌측 메뉴명으로 사용됨.
    * chapters, section은 별도 `caption`이 필요하지 않으며 각기 해당 .md 파일에 # 명칭을 메뉴명으로 연동됨 
* - {bdg-info}`file:`
  - markdown, rst 등 실제 문서 파일
* - {bdg-info}`url:`
  - 외부 사이트 문서 링크
```
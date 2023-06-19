# quickstart

```{note}
1. **install**: jupyter-book library 설치
2. **create**: jupyter sample book 생성
3. **build**: html 파일 생성
4. **browse**: 웹 브라우저로 book 확인
```
## 1. install
* `pdm add jupyter-book(or jb 이하 jb)`
    * 설치 후 `pdm show jupyter-book` 버전 확인
    ```{figure} ./img/jb_01.png
    ```  
+++

## 2. create
* `pdm run jb create {폴더명}`
  * {폴더명} 안에 관련 파일 생성
  * _config.yml, _toc.yml, intro.md 등
      * `_config.yml`: jupyter book 환경 설정 파일
      * `_toc.yml`: 메뉴 구성 파일
      * `intro.md`: 메인화면 구성 파일
+++

## 3. build
* `pdm run jb build {폴더명}`
  * _build 폴더 내 html 파일 생성
      ```{tip}
      * 이전 빌드되었던 내용 삭제(_build 폴더 안 내용)
          * {bdg-info}`pdm run jb clean {폴더명}` or {bdg-info}`pdm run jb build **--all** {폴더명}`
      * clean하지 않을 경우 이전 내용이 캐쉬되어 정상적으로 보여지지 않는 경우 존재
      ```
  * build 성공 후 cli message
      ```none
          Finished generating HTML for book.
          Your book's HTML pages are here:
              docs/_build/html/
          You can look at your book by opening this file in a browser:
              docs/_build/html/index.html
          Or paste this line directly into your browser bar:
              file:///home/yblee/workspace/tdc/docs/_build/html/index.html      
      ```
  * build option
      ```{figure} ./img/jb_build_01.png
      ```
+++

## 4. browse 
  - '_build/html/index.html'을 브라우저로 열면 아래 화면 실행
      ```{figure} ./img/jb_02.png
          :width: 80%
      ```

## 5. configure
    -  {bdg-info}`_config.yml`: jb 환경 설정, sphinx theme 적용 등
    -  {bdg-info}`_toc.yml`: 목차(table of contents) 정의

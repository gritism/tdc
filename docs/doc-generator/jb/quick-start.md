# quickstart

jupyter book library 설치 후 sample book 생성

1. **install**: `pdm add jupyter-book`
    * 설치 후 `pdm show jupyter-book` 버전 확인
    ```{figure} ./img/jb_01.png
    ```  
+++

2. **create**: `pdm run jupyter-book create {폴더명}`
    * {폴더명} 안에 관련 파일 생성
    * _config.yml, _toc.yml, intro.md 등
        * `_config.yml`: jupyter book 환경 설정 파일
        * `_toc.yml`: 메뉴 구성 파일
        * `intro.md`: 메인화면 구성 파일
+++

3. **build**: `pdm run jupyter-book build {폴더명}`
    - _build 폴더 내 html 파일 생성
    - '_build/html/index.html'을 브라우저로 열면 아래 화면 실행
    ```{figure} ./img/jb_02.png
        :width: 80%
    ```
    ```{tip}
    * pdm run jupyter-book clean {폴더명}: 이전 빌드되었던 내용 삭제(_build 폴더 안 내용)
    * clean하지 않을 경우 이전 내용이 캐쉬되어 정상적으로 보여지지 않는 경우 존재
    ```
+++

4. **configure**: `pdm run jupyter-book create {폴더명}`
    - _config.yml
    - _toc.yml

# jupyter-book

``{note}
> Executable Book Project 일환으로 2018년 4월 Beta 버전 출시  
> sphinx 엔진을 기반으로 Jupyter notebook과 결합하여 모듈을 만듬  
> jupyter notebook을 많이 사용하는 데이터 과학자(분석가)들의 활용이 높을 것으로 예상됨
> [github](https://github.com/executablebooks/jupyter-book/releases?page=5)  
``
-------


## quickstart
아래 순서대로 진행하면 sample book을 설치하여 동작 방식 확인 가능
1. **install**: `pdm run jupyter-book`
    * 최상위 프로젝트에서 실행
    * docs 포털 내 sphinx source, build 폴더 등 관련 실행파일 생성  
+++

2. **create**: `pdm run jupyter-book create {폴더명}`
    * generate a sample book 
+++

3. **configure**: `pdm run jupyter-book create {폴더명}`
    - _config.yml
    - _toc.yml
+++

4. **build**: `pdm run jupyter-book build {폴더명}`
    - _build 폴더 내 html 파일 생성

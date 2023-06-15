# github pages

## create repo
* github repository를 public으로 생성 (private의 경우 유료로 github page 서비스 이용 가능)
* github repo 존재한다고 가정하고 아래 내용 시작
  
## 3가지 방법
github pages 연동 방식은 3가지 존재
1) `_build/html` 폴더 내 html 컨텐츠를 수동으로 `gh-pages` branch로 이동 복사
2) `ghp-import 모듈` 활용하는 방법 (여기서 설명)
3) `Github Action` 활용하는 방법 (다음에 설명)

## create pages
* click github repo > setting
* click {bdg-primary}`pages` in left menu
  * Source: select `Deploy from a branch`
  * Branch: select `gh-pages`, `root`
  * Click `save` button
    ```{figure} ./img/ghp_01.png

## `gph-import` 모듈 설치 및 publish
* 모듈 설치: `pdm add ghp-import`
* 모듈 실행: `pdm run gph-import -n -p -f docs/_build/html`
  * 옵션
  * -n: Include a .nojekyll file in the branch.
  * -p: Push the branch to origin/{branch} after committing.
  * -f: Force the push to the repository.
  * 실행결과
    ```none
    Enumerating objects: 389, done.
    Counting objects: 100% (389/389), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (204/204), done.
    Writing objects: 100% (389/389), 5.06 MiB | 2.76 MiB/s, done.
    Total 389 (delta 135), reused 386 (delta 133), pack-reused 0
    remote: Resolving deltas: 100% (135/135), done.
    remote: 
    remote: Create a pull request for 'gh-pages' on GitHub by visiting:
    remote:      https://github.com/yoblee/tdc/pull/new/gh-pages
    remote: 
    To https://github.com/yoblee/tdc.git
    * [new branch]      gh-pages -> gh-pages
    ``` 

## 본인 github page 접속
* https://{github id}.github.io/{book name}



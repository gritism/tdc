---
numbering:
  heading_2: true
---

# github pages
* `github pages`는 github에서 웹 사이트 hosting을 제공하는 서비스 
* `github action`은 workflow 자동화
* 위 2가지를 이용해 github에 등록된 정적 컨텐츠(html, image 등)를 쉽게 호스팅 할 수 있음. 
  (site url --> https://{github_id}.github.io)/directory

## flow
* book 컨텐츠를 작성하고 build 한 후 github pages보 배포 3단계 절차로 이루어지며
  이를 자동화 하기 위해 `github action`을 사용함

<절차>
1. book 컨텐츠 작성 (.md) commit
2. build: .md 파일로 부터 html/image 등 static 파일 생성 
  * 명령어: `jupyter-book build docs/`
  * build 수행하면 `./_build/html` 디렉토리에 관련 artifact 생성됨
3. deploy: `./_build/html` 파일을 github pages에 배포
  * github pages configuration: `deploy from branch` 선택

## 0. github pages 설정
* click github repo > setting
* click {bdg-primary}`pages` in left menu
  * Source: select `Deploy from a branch`
  * Branch: select `gh-pages`, `root`
  * Click `save` button
    ```{figure} ./img/ghp_01.png

## 3가지 방법
github pages 연동 방식은 3가지 존재
1) `_build/html` 폴더 내 html 컨텐츠를 수동으로 `gh-pages` branch로 이동 복사
2) `ghp-import 모듈` 활용하는 방법 (반자동: 여기서 설명)
3) `Github Action` 활용하는 방법 (자동: 다음에 설명)


## `ghp-import` 모듈 설치 및 publish
* 모듈 설치: `pdm add ghp-import`
* 모듈 실행: `pdm run ghp-import -n -p -f docs/_build/html`
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
## github action
* `repo > settings > Pages` 선택
* `Build and deployment` Source를 `Github Actions`로 선택
    ```{figure} ./img/git_action_01.png
* 위 그림 하단 `Github Pages Jekyll` 영역 `Configure` 선택
* 파일을 아래 내용으로 수정 `publish.yml`
  ```
  on:
    # Runs on pushes targeting the default branch
    push:
      branches: ["main"]

    # Allows you to run this workflow manually from the Actions tab
    workflow_dispatch:

  # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
  permissions:
    **contents: write**
    pages: write
    id-token: write

  jobs:
    deploy-book:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v2

      # Install dependencies
      - name: Set up Python 3.10.12
        uses: actions/setup-python@v1
        with:
          python-version: 3.10.12

      - name: Install pdm
        run: |
          pip install pdm

      - name: Install dependencies
        run: |
          pdm install

      # Build the book
      - name: Build the book
        run: |
          pdm run jupyter-book build ./docs/

      # Push the book's HTML to github-pages
      - name: GitHub Pages action
        uses: peaceiris/actions-gh-pages@v3.5.9
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/_build/html
  ```
* repo 상단 메뉴 `action` 탭 선택 > 좌측 메뉴 `pages-build-deployment` 선택 후 우측 `workflow` 선택
    ```{figure} ./img/git_action_02.png

## github page 접속
* https://{github id}.github.io/{book name}



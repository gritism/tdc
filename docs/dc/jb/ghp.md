---
numbering:
  heading_2: true
---
# github pages

--------

```{dropdown} Objective

github pages(web hosting) 및 github action(workflow 자동화)를 이용하여 md 파일로 작성된 book을 호스팅하는 방법

```

## 1. github pages
* `github pages`는 웹 사이트 hosting 제공 서비스임 
* `github action`은 workflow 자동화하는 도구로 `github pages` 컨텐츠 build & deploy 자동화 시 활용함.
* 위 2가지를 이용해 github에 등록된 정적 컨텐츠(html, image 등)를 쉽게 호스팅 할 수 있음. 
  (site url --> https://{github_id}.github.io)/directory

```{note}
:class: dropdown
web hosting process
* book컨텐츠(.md 파일)를 작성하고 웹 호스팅을 위해 html 파일로 전환(build 단계)를 수행한 후
  생성한 html 파일을 github page(웹 서버)로 deploy(배포)하는 3단계 과정을 거쳐야 함.
  > 1) create (.md 작성) -> build (html파일 생성) -> deploy (웹서버 배포)
* 일련의 과정을 자동화 해주기 위해 `github action`을 사용함.
```

## 2. build & deploy

github pages는 2가지 방식으로 deploy 할 수 있음.
```{list-table}
:header-rows: 1
:name: gp_deploy_option

* - 방법
  - 설명
* - `Github Action` (2.1)
  - 로컬에서 컨텐츠(.md, .rst 등) 작성 후 github repo.에 commit하면 자동으로 github pages에 build & deploy
* - `Deploy from a branch` (2.2)
  - 로컬에서 컨텐츠(.md, .rst 등) 작성 후 gph-import 모듈이용하여 gh-pages branch에 업로드하면 자동으로 github page에 deploy
```

### 2.1 github action  

#### 2.1.1 github pages config

>  ```{image} ./img/ghp_02.png
>  ```

#### 2.1.2. .yml 파일 생성  
>  ```{code-block}
>  # Sample workflow for building and deploying a Jekyll site to GitHub Pages
>  name: deploy book
>
>  on:
>    # Runs on pushes targeting the default branch
>    push:
>      branches: ["main"]
>
>    # Allows you to run this workflow manually from the Actions tab
>    workflow_dispatch: 
>
>  # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
>  permissions:
>    contents: write
>    pages: write
>    id-token: write
>
>  jobs:
>    publish:
>      runs-on: ubuntu-latest
>      steps:
>      - uses: actions/checkout@v2
>
>      # Install dependencies
>      - name: Set up Python 3.10.12
>        uses: actions/setup-python@v1
>        with:
>          python-version: 3.10.12
>
>      - name: Install pdm
>        run: |
>          pip install pdm
>
>      - name: Install dependencies
>        run: |
>          pdm install
>
>      # Build the book
>      - name: Build the book
>        run: |
>          pdm run jupyter-book build ./docs/
>
>      # publish
>      - name: Upload artifact
>        uses: actions/upload-pages-artifact@v1
>        with:
>          # Upload entire repository
>          path: './docs/_build/html/'
>      - name: Upload artifact
>        uses: actions/upload-artifact@v3
>        with:
>          # Upload entire repository
>          path: './docs/_build/html/'
>      - name: Deploy to GitHub Pages
>        id: publish
>        uses: actions/deploy-pages@v2
>  ```

#### 2.1.3. github pages 접속 확인  

>  ```{image} ./img/ghp_site_01.png
>  ```

#### 2.1.4. example repository  
  * 아래 site에서 참조 (https://github.com/yoblee/book_deploy)

### 2.2 deploy from a branch 

#### 2.2.1. github pages config
 * click github repo > setting, then click {bdg-primary}`pages` in left menu
   * Source: `Deploy from a branch`, Branch: `gh-pages`, `root` 선택 후 `save`
     ```{figure} ./img/ghp_01.png

#### 2.2.2. ghp-import 설치 및 배포  

  ghp-import 모듈을 이용하여 build 후 `gh-pages` branch로 자동 배포
  * 모듈 설치: `pdm add ghp-import`
  * 모듈 실행: `pdm run ghp-import -n -p -f docs/_build/html`
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

    ```{note}
    :class: dropdown
    - n: Include a .nojekyll file in the branch.
    - p: Push the branch to origin/{branch} after committing.
    - f: Force the push to the repository.
    ```

#### 2.2.3. github pages 접속 확인
  * https://{github id}.github.io/{book name}

##### build 자동화 - github action
* github > Actions 선택
* `New workflow` 선택 후 아래 내용 작성 후 commit (`publish.yml`)
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


.. role:: raw-html-m2r(raw)
   :format: html


sphinx
======

..

   python 기반 문서 자동 생성 라이브러리임\ :raw-html-m2r:`<br>`
   공식 `python document <https://docs.python.org/ko/3/>`_\ 도 sphinx 기반\ :raw-html-m2r:`<br>`
   `readthedocs <https://readthedocs.org/>`_\ 도 sphinx기반으로 구현됨


----

install
-------


* (pip) pip install sphinx
* (pdm) pdm add sphinx

quickstart
----------


* 
  **config**\ : ``pdm run sphinx-quickstart docs``


  * 최상위 프로젝트에서 실행
  * docs 포털 내 sphinx source, build 폴더 등 관련 실행파일 생성

* 
  **create**\ : ``pdm run sphinx-apidoc -o docs/source . -e``


  * python 소스 파일(패키지, 모듈)로 부터 document generation
  * 소스 내 docstring(주석) 내용을 읽어서 문서화 하는 것으로 docstring 작성 규칙에 따라 주석을 작성해야 함.
  * 
    이를 위해서는 conf.py 파일 수정 필요

    .. code-block::

         import sys, os
         # sys.path.append(os.path.abspath('sphinxext'))
         sys.path.insert(0, os.path.abspath('../../../'))

         extensions = ['sphinx.ext.autodoc']

    ..

       ``usage: sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN, ...]``


* 
  **build**\ : ``pdm run sphinx-build docs/source docs/build/html``


  * sphinx source(.rst, .md 등) 파일을 읽어서 html(default) 등 다양한 형태 문서파일로 전환
    ..

       ``usage: sphinx-build [OPTIONS] SOURCEDIR OUTPUTDIR [FILENAMES...]``
       ※ make html로 실행해도 됨


목차 만들기
-----------


* 
  index.rst 수정


  * (caption) 제목
  * 
    python/pandas.md 가 페이지 명

    .. code-block::

       .. toctree::
         :maxdepth: 2
         :caption: python:

         python/pandas.md
         python/seaborn.md
         python/sphnix.md

jupyter notebook 사용
---------------------


* nbsphinx 설치

  * ``pdm add nbsphinx``

* myst-NB 설치

  * ``pdm add myst-nb``

markdown 사용
-------------


* myst_parser 이용

  #. myst_parser 라이브러리 설치

     * ``pdm add myst_parser``

  #. conf.py 수정

     * ``extensions = ['myst_parser']``

  #. index.rst 수정

     * markdown 명 추가

* 
  m2r 이용

  ..

     myst_parser의 경우 md가 정확히 전환되지 않는 경우 존재하여 m2r로 이용



  #. m2r 라이브러리 설치

     * ``pdm add m2r``

  #. conf.py 수정

     * ``extensions = ['m2r']``

  #. index.rst 수정

     * ``.. mdinclude:: ../../파일명.md``

theme
-----


* readthedocs theme 적용

  * theme 설치
    ..

       ``pdm add sphinx_rtd_theme``


  * conf.py 파일 수정
    ..

       ``html_theme = 'sphinx_rtd_theme'``


* readthedocs theme 적용

  * theme 설치
    ..

       ``pdm add sphinx_rtd_theme``


  * conf.py 파일 수정
    ..

       ``html_theme = 'sphinx_rtd_theme'``


Error
-----


* ``WARNING: invalid signature for automodule``
  ..

     프로젝트 또는 패키지명에 '-'(대시) 이 존재하는 경우


* ``ERROR: Theme error``
  ..

     sphinx 7.x에서 rth_theme 오류 발생, 오류 패치 전까지 하위 버전 활용 (6.x)


* ``ERROR: no module``

  * conf.py 파일 수정
    .. code-block::

         import sys, os
         # sys.path.append(os.path.abspath('sphinxext'))
         sys.path.insert(0, os.path.abspath('../../../'))

* ``ERROR: RTD/Sphinx not rendering bullet list from rst file``
  ..

     sphinx-rtd-theme 0.5.1 버전일 경우 발생 최신 버전으로 upgrade


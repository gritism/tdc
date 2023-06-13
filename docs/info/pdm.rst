.. role:: raw-html-m2r(raw)
   :format: html


pdm
---

..

   Python 라이브러리 패키지 관리 모듈 (poetry 등 존재)\ :raw-html-m2r:`<br>`
   modern **Python package and dependency manager** supporting the latest PEP standards  

   ..

      ※ PEP (Python Enhancement Proposal)\ :raw-html-m2r:`<br>`
      ※ `pdm document <https://pdm.fming.dev/latest/>`_\ :raw-html-m2r:`<br>`
      ...


----


#. 
   설치


   * ``pip install pdm``
   * PDM 버전 확인: ``pdm --version``

#. 
   초기화


   * ``pdm init``
     ..

        Initialize a pyproject.toml for PDM\ :raw-html-m2r:`<br>`
        해당 디렉토리 아래 pyproject.toml 파일 생성\ :raw-html-m2r:`<br>`
        pyproject.toml 파일에 설치된 python library 목록 생성됨


   * ``pdm install``
     ..

        Install dependencies from lock file (pyproject.toml)


#. 
   python library 설치


   * StockAnalysis 관련 필요 라이브러리 설치: pdm install
   * 개별 라이브러리 설치: pdm add {라이브러리명} ex) pdm add pandas

#. 
   설치 목록 조회


   * ``pdm list``

#. 
   빌드


   * ``pdm build``

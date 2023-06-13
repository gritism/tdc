.. role:: raw-html-m2r(raw)
   :format: html


wsl :raw-html-m2r:`<sup>window subsystem linux</sup>`
---------------------------------------------------------

..

   윈도우에서 리눅스를 사용할 수 있는 가상환경 프로그램  

   ..

      `wsl document <https://learn.microsoft.com/ko-kr/windows/wsl/install>`_\ :raw-html-m2r:`<br>`
      ...


----


#. 
   설치


   * 윈도우 cmd 또는 powershell 실행 후
   * ``wsl -install`` (설치 후 재시작)

#. 
   설치 확인 및 실행


   * 윈도우 리부팅 후 cmd 창에서 아래 명령어 실행
   * ``wsl -l -v``

#. 
   윈도우 터미널 설치


   * MS store에서 윈도우 터미널 다운로드 및 설치

#. 
   VSC 환경 설정 (Remote 환경: WSL연동)


   * VSC 다운로드 및 설치 후 아래 2개 extension 설치
   * Remote-SSH
   * WSL
   * 윈도우 터미널(WSL)에서 ``code .`` 입력하면 VSC 실행되고 ``explorer.exe .`` 실행하면 윈도우 탐색기 열림

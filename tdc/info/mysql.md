## mysql
> 관계형 데이터 구조를 관리하기 위한 database program,  
> 오픈 소스로 시작하여 기업용은 별도 라이선스 구매 필요.  
> [mysql document](https://www.mysql.com/support/)  
> ...

-------

1. 설치
    - 리눅스 mysql 서버 설치: `sudo apt-get install mysql-server`
    - 외부 접속 허용: `sudo ufw allow mysql`
    - mysql 시작: `sudo systemctl start mysql`
    - mysql 자동 재시작(Ubuntu 재기동 시): `sudo systemctl enable mysql`

2. DB/사용자 생성 및 권한 부여
    - DB 생성: `create database {db_name}`;
    - 사용자 생성: `CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin1234'`;
    - 권한 부여: `GRANT ALL PRIVILEGES ON STOCKDB.* to 'admin'@'localhost'`;
    - `flush privileges`;
    - StockAnalysis 관련 table 및 데이터 생성: `pdm run StockDB/DBUpdater.py`

3. error
    - Can't connect to local MySQL server through socket
    > `sudo service mysql restart`

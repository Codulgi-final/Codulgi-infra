# MariaDB의 공식 이미지를 기반으로 사용
FROM mariadb:10.7

# 환경 변수 설정 (root 패스워드 설정)
ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=codulgi_db
ENV MYSQL_USER=codulgi
ENV MYSQL_PASSWORD=codul1234

# 기본 포트 3306 노출
EXPOSE 3306

# MariaDB에 데이터베이스 초기화 시 스크립트를 실행할 수 있도록 설정
COPY init.sql /docker-entrypoint-initdb.d/

# 데이터베이스와 관련된 설정 파일 복사 (필요시)
# COPY my.cnf /etc/mysql/my.cnf

# MariaDB 기본 동작
CMD ["mysqld"]

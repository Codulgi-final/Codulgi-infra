-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS codulgi_db;

-- 사용자 생성 및 비밀번호 설정
CREATE USER IF NOT EXISTS 'codulgi'@'%' IDENTIFIED BY 'codul1234';

-- 해당 사용자에게 데이터베이스 권한 부여
GRANT ALL PRIVILEGES ON codulgi_db.* TO 'codulgi'@'%';

-- 권한 적용
FLUSH PRIVILEGES;


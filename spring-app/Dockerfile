# 1. OpenJDK 이미지를 베이스로 사용
FROM openjdk:17-jdk-slim


# 2. wait.sh 스크립트를 컨테이너로 복사하고 실행 권한 부여
RUN apt-get update && apt-get install -y netcat-openbsd
COPY wait.sh /wait.sh
RUN chmod +x /wait.sh

# 3. JAR 파일을 /app 디렉터리로 복사
COPY ./codulgi-server-0.0.1-SNAPSHOT.jar /app/codulgi-server-0.0.1-SNAPSHOT.jar

# 4. 애플리케이션 실행 명령을 wait.sh 스크립트를 통해 실행
ENTRYPOINT ["/wait.sh", "java", "-jar", "/app/codulgi-server-0.0.1-SNAPSHOT.jar", "--spring.profiles.active=prod"]

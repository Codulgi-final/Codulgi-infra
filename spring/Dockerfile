# 1. OpenJDK 이미지를 베이스로 사용
FROM openjdk:17-jdk-slim

# 2. JAR 파일을 /app 디렉터리로 복사
COPY ./TripCok-0.0.1-SNAPSHOT.jar /app/TripCok-0.0.1-SNAPSHOT.jar

# 3. 포트 설정 (Spring 애플리케이션이 사용하는 포트)
EXPOSE 8080

# 4. 애플리케이션 실행 명령
ENTRYPOINT ["java", "-jar", "/app/TripCok-0.0.1-SNAPSHOT.jar"]

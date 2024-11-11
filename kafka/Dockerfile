# 기본 이미지 선택 (예: OpenJDK 11 사용)
FROM openjdk:11-jre

# Kafka 버전과 Scala 버전 설정
ENV KAFKA_VERSION=3.7.1
ENV SCALA_VERSION=2.13

# Kafka 설치 폴더 설정
ENV KAFKA_HOME=/opt/kafka

# Kafka 다운로드 및 압축 해제
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://downloads.apache.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && \
    mkdir -p $KAFKA_HOME && \
    tar -xzf kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C $KAFKA_HOME --strip-components=1 && \
    rm kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

# 데이터 디렉토리 생성
RUN mkdir -p /tmp/kafka-logs

# 환경 변수 설정
ENV PATH="${PATH}:${KAFKA_HOME}/bin"

# 포트 설정
EXPOSE 9092 2181

# 시작 스크립트 복사
COPY start-kafka.sh /usr/bin/start-kafka.sh
RUN chmod +x /usr/bin/start-kafka.sh

# 기본 실행 명령
CMD ["start-kafka.sh"]

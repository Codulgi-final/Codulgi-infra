# 기본 이미지 선택 (예: OpenJDK 11 사용)
FROM openjdk:11-jre

# Zookeeper 버전 설정
ENV ZOOKEEPER_VERSION=3.8.0

# Zookeeper 설치 폴더 설정
ENV ZOOKEEPER_HOME=/opt/zookeeper

# Zookeeper 다운로드 및 압축 해제
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://downloads.apache.org/zookeeper/stable/apache-zookeeper-${ZOOKEEPER_VERSION}-bin.tar.gz && \
    mkdir -p $ZOOKEEPER_HOME && \
    tar -xzf apache-zookeeper-${ZOOKEEPER_VERSION}-bin.tar.gz -C $ZOOKEEPER_HOME --strip-components=1 && \
    rm apache-zookeeper-${ZOOKEEPER_VERSION}-bin.tar.gz

# Zookeeper 실행을 위한 설정 (기본 설정 파일 사용)
COPY zoo.cfg /opt/zookeeper/conf/

# 포트 노출 (Zookeeper 기본 포트)
EXPOSE 2181 2888 3888

# Zookeeper 실행 명령
CMD ["/opt/zookeeper/bin/zkServer.sh", "start-foreground"]

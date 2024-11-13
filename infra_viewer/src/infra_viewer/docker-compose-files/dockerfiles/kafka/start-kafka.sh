#!/bin/bash

# Zookeeper 시작
$KAFKA_HOME/bin/zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties

# Kafka 설정: 호스트 이름 및 기본 포트로 브로커 ID 설정
#변경 전
#export KAFKA_BROKER_ID=${KAFKA_BROKER_ID:-1}
#export KAFKA_LISTENERS=${KAFKA_LISTENERS:-PLAINTEXT://:9092}

#변경 후
export KAFKA_BROKER_ID=0
export KAFKA_LISTENERS=PLAINTEXT://:9092


export KAFKA_LOG_DIRS=/tmp/kafka-logs

# ZooKeeper에서 Kafka 노드 삭제 (broker.id=0)
$KAFKA_HOME/zkCli.sh -server zookeeper:2181 delete /brokers/ids/0

# Kafka 서버 시작
echo "Starting Kafka server..."
$KAFKA_HOME/kafka-server-start.sh /opt/kafka/config/server.properties

# Kafka 시작
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties

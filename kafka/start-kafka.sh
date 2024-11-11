#!/bin/bash

# Zookeeper 시작
$KAFKA_HOME/bin/zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties

# Kafka 설정: 호스트 이름 및 기본 포트로 브로커 ID 설정
export KAFKA_BROKER_ID=${KAFKA_BROKER_ID:-1}
export KAFKA_LISTENERS=${KAFKA_LISTENERS:-PLAINTEXT://:9092}
export KAFKA_LOG_DIRS=/tmp/kafka-logs

# Kafka 시작
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties

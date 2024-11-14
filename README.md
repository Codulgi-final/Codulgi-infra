### 개요
개발 구성원 누구나 노트북 하나로 동일한 환경을 활용할 수 있게 하며, Prometheus와 Grafana로 모니터링 지표를 시각화하고, scale 조정을 효율적으로 관리할 수 있도록 설계

Docker Compose를 토대로 프로젝트 진행

### 요구사항
모니터링 시스템 구축
- Prometheus를 사용하여 시스템 및 애플리케이션 지표를 수집
- Grafana를 활용해 실시간으로 대시보드를 통해 지표를 시각화
- 각 구성 요소에 대한 Exporter를 설정하여 지표 수집을 세부적으로 구성

Scale 조정 관리 화면
- 사용자가 수동으로 scale을 조절할 수 있는 인터페이스를 제공
- 자동 및 수동 scale 조정 기록을 히스토리 형식으로 저장하고 조회할 수 있도록 설정
- 필요에 따라 scale 조정 작업을 관리할 수 있는 권한 및 알림 시스템을 추가

![image](https://github.com/user-attachments/assets/4a5ccee2-d38e-4572-aa46-26b48479e71e)

```bash
$ docker compose -f airflow-docker-compose.yml up -d
$ docker compose -f spark-docker-compose.yml up -d
$ docker compose -f kafka-docker-compose.yml up -d
$ docker compose -f spring-docker-compose.yml up -d
```

```bash
$ docker compose -f airflow-docker-compose.yml down
$ docker compose -f spark-docker-compose.yml down
$ docker compose -f kafka-docker-compose.yml down
$ docker compose -f spring-docker-compose.yml down
```

```bash
# airflow 설치 
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'

참조 url: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

```

```bash
# spark 설치 
참조 url: https://github.com/bitnami/containers/blob/main/bitnami/spark/docker-compose.yml
```

```bash
# kafka 설치 

참조 url 
```

### spring-docker-compose up 하기 전
$ docker volume prune
$ docker buildx prune
$ docker rmi $(docker images -a -q)
$ docker rm -f $(docker ps -a -q)

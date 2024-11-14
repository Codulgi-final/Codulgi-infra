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

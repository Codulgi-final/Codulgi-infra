
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

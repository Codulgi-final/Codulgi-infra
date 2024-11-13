import os
import subprocess
from fastapi import HTTPException

# Docker Compose 파일이 있는 디렉토리 설정
COMPOSE_DIR = "/infra_viewer/docker-compose-files"

# Docker Compose 파일 이름을 서비스 이름에 매핑
compose_files = {
    "airflow": os.path.join(COMPOSE_DIR, "airflow-docker-compose.yml"),
    "grafana": os.path.join(COMPOSE_DIR, "grafana-prometheus-compose.yml"),
    "kafka": os.path.join(COMPOSE_DIR, "kafka-docker-compose.yml"),
    "spark": os.path.join(COMPOSE_DIR, "spark-docker-compose.yml"),
    "spring": os.path.join(COMPOSE_DIR, "spring-docker-compose.yml")
}


def execute_docker_compose(service: str, action: str):
    if service not in compose_files:
        raise HTTPException(status_code=404, detail="Service not found")

    compose_file = compose_files[service]
    command = ["docker-compose", "-f", compose_file, action]
    if action == "up":
        command.append("-d")

    try:
        subprocess.run(command, check=True)
        return {"status": "success", "action": action, "service": service}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to {action} {service}: {e}")

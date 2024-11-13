import os
import subprocess
import json
from fastapi import HTTPException

COMPOSE_DIR = "./docker-compose-files"


def list_compose_files():
    """docker-compose-files 폴더의 모든 YAML 파일을 목록으로 반환"""
    return [f for f in os.listdir(COMPOSE_DIR) if f.endswith('.yml')]


def run_compose_file(file_name):
    """Docker Compose 파일 실행"""
    compose_path = os.path.join(COMPOSE_DIR, file_name)
    subprocess.run(["docker-compose", "-f", compose_path, "up", "-d", "--build"], check=True)


def stop_compose_file(file_name):
    """Docker Compose 파일 중지"""
    compose_path = os.path.join(COMPOSE_DIR, file_name)
    subprocess.run(["docker-compose", "-f", compose_path, "down"], check=True)


def stop_all_containers():
    """모든 컨테이너 중지 및 삭제"""
    for file_name in list_compose_files():
        compose_path = os.path.join(COMPOSE_DIR, file_name)
        subprocess.run(["docker-compose", "-f", compose_path, "down"], check=True)


def get_container_stats(container_id: str):
    """특정 컨테이너의 CPU 및 메모리 사용량 정보를 가져옵니다."""
    try:
        stats_result = subprocess.run(
            ["docker", "stats", "--no-stream", "--format", "{{json .}}", container_id],
            capture_output=True,
            text=True,
            check=True
        )
        stats_data = json.loads(stats_result.stdout.strip())
        return {
            "cpu_percent": stats_data["CPUPerc"].replace('%', ''),
            "memory_usage": stats_data["MemUsage"].split(" / ")[0],
            "memory_limit": stats_data["MemUsage"].split(" / ")[1]
        }
    except subprocess.CalledProcessError as e:
        print(f"Failed to get stats for container {container_id}: {e}")
        return {"cpu_percent": "N/A", "memory_usage": "N/A", "memory_limit": "N/A"}


def list_containers():
    """현재 실행 중인 모든 컨테이너 정보를 가져옵니다."""
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{json .}}"],
            capture_output=True,
            text=True,
            check=True
        )

        containers_info = []
        for line in result.stdout.splitlines():
            container_data = json.loads(line)
            container_id = container_data["ID"]

            # 컨테이너의 CPU 및 메모리 사용량을 가져옵니다.
            stats = get_container_stats(container_id)

            # 메모리 사용률 계산
            try:
                memory_usage = float(stats["memory_usage"].replace("MiB", "").strip())
                memory_limit = float(stats["memory_limit"].replace("MiB", "").strip())
                memory_usage_percent = (memory_usage / memory_limit) * 100 if memory_limit > 0 else "N/A"
            except ValueError:
                memory_usage_percent = "N/A"

            containers_info.append({
                "id": container_data["ID"],
                "name": container_data["Names"],
                "status": container_data["Status"],
                "ports": container_data["Ports"],
                "cpu_percent": stats["cpu_percent"],
                "memory_usage": stats["memory_usage"],
                "memory_limit": stats["memory_limit"],
                "memory_usage_percent": memory_usage_percent
            })

        return containers_info

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to list containers: {e}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse container data: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

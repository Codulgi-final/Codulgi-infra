import subprocess
import json
from fastapi import HTTPException


def get_container_stats(container_id: str):
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


def list_containers():
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

            # 컨테이너의 리소스 사용량을 가져옵니다.
            try:
                stats = get_container_stats(container_id)
            except subprocess.CalledProcessError as e:
                stats = {"cpu_percent": "N/A", "memory_usage": "N/A", "memory_limit": "N/A"}
                print(f"Failed to get stats for container {container_id}: {e}")

            containers_info.append({
                "id": container_data["ID"],
                "name": container_data["Names"],
                "status": container_data["Status"],
                "ports": container_data["Ports"],
                **stats  # cpu_percent, memory_usage, memory_limit 추가
            })

        return containers_info

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch container data: {e}")

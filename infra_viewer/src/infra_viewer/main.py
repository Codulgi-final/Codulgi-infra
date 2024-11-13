# main.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles

from docker_utils.docker_manager import (
    list_compose_files,
    run_compose_file,
    stop_compose_file,
    stop_all_containers,
    list_containers
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class ExecuteOrderRequest(BaseModel):
    files: list


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    compose_files = list_compose_files()
    return templates.TemplateResponse("index.html", {"request": request, "compose_files": compose_files})


# 순서대로 실행
@app.post("/execute-order")
async def execute_in_order(request: ExecuteOrderRequest):
    try:
        for file_name in request.files:
            run_compose_file(file_name)
        return {"status": "success", "message": "모든 컨테이너 실행에 성공하였습니다."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute files in order: {str(e)}")


# 모든 컨테이너 중지 및 삭제
@app.post("/stop-all-containers")
async def stop_all_containers_endpoint():
    try:
        stop_all_containers()
        return {"status": "success", "message": "모든 컨테이너를 종료 후 삭제하였습니다."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to stop and remove all containers: {str(e)}")


# 개별 Docker Compose 파일 실행
@app.post("/services/{file_name}/up")
async def start_compose_service(file_name: str):
    try:
        run_compose_file(file_name)
        return {"status": "success", "message": f"{file_name} 컨테이너가 시작되었습니다."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start {file_name}: {str(e)}")


# 개별 Docker Compose 파일 중지
@app.post("/services/{file_name}/down")
async def stop_compose_service(file_name: str):
    try:
        stop_compose_file(file_name)
        return {"status": "success", "message": f"{file_name} 컨테이너가 중지되었습니다."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to stop {file_name}: {str(e)}")


@app.get("/api/containers")
async def get_containers():
    try:
        containers = list_containers()
        return containers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch container data: {str(e)}")

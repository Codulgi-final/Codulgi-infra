# 기본 이미지로 Airflow의 공식 이미지를 사용
FROM apache/airflow:2.6.2

# Airflow의 사용자 및 그룹 설정
USER root

# 추가적인 파이썬 패키지나 라이브러리 설치 (필요한 경우)
RUN pip install --no-cache-dir \
    apache-airflow-providers-mysql \
    apache-airflow-providers-postgres

# 작업 디렉토리 설정
WORKDIR /opt/airflow

# 환경 변수 설정 (필요에 따라 변경 가능)
ENV AIRFLOW_HOME=/opt/airflow

# 기본적으로 필요한 데이터베이스 연결 환경 변수 설정
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=mysql://root:root_password@mysql:3306/airflow

# Airflow 웹 서버와 스케줄러가 함께 실행될 수 있도록 CMD 설정
CMD ["bash", "-c", "airflow db upgrade && airflow webserver & airflow scheduler"]

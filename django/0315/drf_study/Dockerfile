FROM python:3.11 
# 이미지 설정
LABEL authors="max"
# 작성자
WORKDIR /app
# 작업 디렉토리 설정

#  프로젝트의 의존성 파일을 컨테이너 내부로 복사한다.
COPY requirements.txt /app/

# 의존성 설치
RUN pip install -r requirements.txt

# 나머지 프로젝트 파일들을 컨테이너 내부로 복사한다.
COPY . /app/

EXPOSE 8000
# 8000포트로 노출


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# Docker 컨테이너가 시작될 때 실행될 명령어를 지정한다. 여기서는 Django 개발 서버를 실행한다.
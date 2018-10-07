FROM python:3.6.1-slim
WORKDIR /root/app
EXPOSE 8000
RUN pip install -U pip setuptools
COPY manage.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY nyit nyit
RUN ["python", "manage.py", "runserver"]

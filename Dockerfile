FROM python:3.6.1-slim
WORKDIR /root/app
EXPOSE 8000
RUN pip install -U pip setuptools
ADD manage.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD nyit nyit
CMD ["python", "manage.py", "runserver"]

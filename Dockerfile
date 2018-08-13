FROM python:3.6.1-slim

RUN pip install -U pip setuptools

COPY manage.py .
COPY requirements.txt .
COPY nyit nyit

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]

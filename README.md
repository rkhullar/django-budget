## Django Budget

Simple budget manager application written with django and deployed on AWS with postgres.

### Requirements
- python version 3.6.1
- postgres version 10.4


### Notes

#### Environment Setup
``` sh
python -m venv venv
. venv/bin/activate
pip install -U pip setuptools
pip install -r requirement.txt
pip install nose
```

### Django Structure Setup
``` sh
django-admin startproject nyit .
django-admin startapp budgets
```

FROM python:3.12

COPY requirements.txt /tmp
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
COPY ./ /app

WORKDIR /app

CMD python manage.py runserver 0.0.0.0:8000

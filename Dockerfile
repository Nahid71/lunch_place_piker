FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN echo yes | python manage.py reset_db -c
RUN python manage.py migrate
RUN python manage.py loaddata user/fixtures/myuser.json
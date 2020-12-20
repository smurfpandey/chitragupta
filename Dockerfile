FROM arm32v7/python:3.7-slim-buster

# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt update && apt install -y libpq5
RUN pip install pipenv

# set work directory
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pipenv install --system --deploy --skip-lock

CMD [ "gunicorn", "-b 0.0.0.0:5000", "chitragupta.app:create_app()"]
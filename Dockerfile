FROM python:3.9-slim

# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install pipenv

# set work directory
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "gunicorn", "-b 0.0.0.0:5000", "chitragupta.app:create_app"]
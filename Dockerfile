FROM python:3.9-slim-buster
RUN pip install pipenv

# set work directory
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pipenv install --system --deploy

CMD [ "gunicorn", "--bind 0.0.0.0:5000", "chitragupta.app:create_app()"]
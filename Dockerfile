FROM python:3.9-alpine
RUN pip install pipenv

# set work directory
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "gunicorn", "--bind 0.0.0.0:5000", "-k gevent", "chitragupta.app:create_app()"]
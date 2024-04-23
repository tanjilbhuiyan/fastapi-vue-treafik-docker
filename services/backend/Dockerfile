# pull the official docker image
FROM python:3.12.2-slim
# Copying app directory content to container app directory 
COPY /app /app
# Copy pyproject.toml to app
COPY pyproject.toml /app 
# set work directory
WORKDIR /app
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
# install dependencies
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

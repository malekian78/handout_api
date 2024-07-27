FROM python:3.11

# Fix python printing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installing all python dependencies
ADD requirements/ requirements/
RUN pip install -r requirements/local.txt

# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/

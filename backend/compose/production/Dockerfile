FROM python:3.11

# Installing all python dependencies
ADD requirements/ requirements/
RUN pip install -r requirements/production.txt

COPY ./compose/production/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/production/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/

RUN python manage.py collectstatic --no-input

ENTRYPOINT ["/entrypoint"]

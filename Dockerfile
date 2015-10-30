FROM python:2.7
EXPOSE 5000
ADD . /code
WORKDIR /code
RUN pip install Flask
ENTRYPOINT python -u webapp.py
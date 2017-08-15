FROM python:2.7
EXPOSE 5000
ADD . /code
WORKDIR /code
# six is the dependence of healthcheck
RUN pip install Flask healthcheck six==1.10.0
HEALTHCHECK CMD ["curl", "-f", "http://localhost:5000/health"]
ENTRYPOINT python -u webapp.py
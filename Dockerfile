FROM python:3.5

ADD . /leginx
WORKDIR /leginx
RUN pip install -e .

EXPOSE 8080

CMD ["leginx", "start", "master-conf.yaml"]

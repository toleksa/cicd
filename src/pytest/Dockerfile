FROM python:3.10-slim
RUN pip install pytest requests
RUN apt update ; apt -y install iputils-ping
COPY test_web.py .

CMD pytest --junit-xml=test_result.xml test.py


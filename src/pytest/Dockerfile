FROM python:3.10-slim
RUN pip install pytest requests

WORKDIR /pytest
COPY test_web.py .
CMD pytest --junit-xml=test_result.xml test_web.py


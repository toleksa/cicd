FROM alpine:3.16.0
RUN apk add --no-cache python3 py3-pytest

WORKDIR /pytest
COPY src/python-http/ ./
CMD pytest --junit-xml=test_unit.xml test_unit.py


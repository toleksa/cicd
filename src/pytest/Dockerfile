FROM alpine:3.15.0
RUN apk add --no-cache python3 py3-pytest py3-requests

WORKDIR /pytest
COPY test_web.py .
CMD pytest --junit-xml=test_result.xml test_web.py


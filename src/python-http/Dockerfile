FROM alpine:3.11.0

RUN apk add --no-cache python3

EXPOSE 80
STOPSIGNAL SIGTERM
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1:80 || exit 1

WORKDIR /www
COPY www/* ./
#TODO: should use CMD, but Jenkins fails
ENTRYPOINT python3 -m http.server 80
CMD sh
#CMD python3 -m http.server 80


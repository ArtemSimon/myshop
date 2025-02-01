FROM python:3.12.2-alpine3.19 AS builder

COPY requirements.txt /tmp
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && rm -rf /var/cache/pip
COPY ./ /app

FROM alpine:3.21.2
RUN apk --no-cache upgrade && \
    apk --no-cache add tzdata libffi \
    apk add --no-cache expat
COPY --from=builder /usr/local/bin/python3 /usr/local/bin/python3
COPY --from=builder /usr/local/bin/python3.12 /usr/local/bin/python3.12
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/lib/libpython3.12.so.1.0 /usr/local/lib/libpython3.12.so.1.0
COPY --from=builder /usr/local/lib/libpython3.so /usr/local/lib/libpython3.so
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/ /usr/local/lib/

COPY ./ /app
COPY ./manage.py /app

WORKDIR /app


CMD python manage.py runserver 0.0.0.0:8000

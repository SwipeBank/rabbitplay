FROM python:2.7.10

COPY requirements.txt /app/requirements.txt
RUN set -x \
    && pip install --no-cache-dir -r /app/requirements.txt

#COPY ./certs/ /certs/
COPY ./examples/ /app/examples/
COPY ./amqp/ /app/amqp/

WORKDIR /app/

CMD ["python","-m","examples.receive"]

FROM python:3.6.4

ARG FOREX_PORT
ENV FOREX_PORT=${FOREX_PORT}
ARG FOREX_HOST
ENV FOREX_HOST=${FOREX_HOST}

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE ${FOREX_PORT}

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
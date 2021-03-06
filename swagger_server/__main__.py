#!/usr/bin/env python3

import connexion
import os
from swagger_server import encoder

try:
    PORT = os.environ["FOREX_PORT"]
except KeyError:
    raise ValueError("Must have environment variable FOREX_PORT defined to run this server")

try:
    HOST = os.environ["FOREX_HOST"]
except KeyError:
    raise ValueError("Must have environment variable FOREX_HOST defined to run this server")


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Currency Converter'})
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
'''
index page for flask
displays status and converter
'''
from flask import jsonify, request, abort
from api.v1.views import app_views
from forex_python.converter import CurrencyRates, Decimal
from datetime import datetime
import geocoder

@app_views.route('/status')
def getStatus():
    return jsonify({'status': 'OK'})


@app_views.route('/convert')
def getConversion():
    query = {}
    c = CurrencyRates()
    query['to'] = request.args.get('to')
    query['from'] = request.args.get('from')
    query['amount'] = request.args.get('amt')
    result = c.convert(query['from'], query['to'],
                       Decimal(query['amount']))
    info = {"timestamp": str(datetime.now()),
            "rate": c.get_rate(query['from'], query['to'])}
    return jsonify({"query":query, "info":info, "result": result})

@app_views.route('/locate/')
@app_views.route('/locate/<location>' )
def getCoords(location='me'):
    if location == 'me' or '.' in location:
        g = geocoder.ip(location)
    else:
        g = geocoder.google(location)
    return jsonify(g.json)

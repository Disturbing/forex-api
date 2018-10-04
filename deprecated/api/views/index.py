#!/usr/bin/python3
'''
index page for flask
displays status and converter
'''
from flask import jsonify, request, abort
from api.views import app_views
from forex_python.converter import(CurrencyRates, Decimal,
                                   RatesNotAvailableError)
from datetime import datetime
import geocoder

c = CurrencyRates()

@app_views.route('/status', methods=['GET'])
def getStatus():
    return jsonify({'status': 'OK'})

@app_views.route('/get_rates/<currency>', methods=['GET'])
@app_views.route('/get_rates', methods=['GET'])
def getRate(currency=None):
    query = request.args.copy()
    query['timestamp'] = str(datetime.now())
    if currency:
        try:
            dt = query.get('on')
            if dt:
                dt = datetime.strptime(dt, '%Y-%m-%d')
                query['on'] = dt.strftime("%A, %B %d, %Y")
            query['target'] = currency
            query['rates'] = c.get_rates(currency, dt)
            return jsonify(query)
        except ValueError:
            abort(400, 'invalid date')
        except RatesNotAvailableError:
            abort(400, 'invalid rate')
        except:
            abort(404)
    elif request.args:
        try:
            _to = query.get('to')
            _from = query.get('from')
            query['rate'] = c.get_rate(_from, _to)
            return jsonify(query)
        except:
            abort(400, 'invalid arguments')
    else:
        abort(404, 'no arguments')

@app_views.route('/convert', methods=['GET'])
def getConversion():
    if request.args:
        _from = request.args.get('from')
        if not _from:
            abort(400, "missing field: from")
        _to = request.args.get('to')
        if not _to:
            abort(400, "missing field: to")
        _amt = request.args.get('amt')
        if not _amt:
            abort(400, "missing field: amt")
        try:
            result = c.convert(_from, _to, Decimal(_amt))
            info = {"timestamp": str(datetime.now()),
                    "rate": c.get_rate(_from, _to)}
            return jsonify({"query":request.args,
                            "info":info, "result": result})
        except:
            abort(400, 'invalid arguments')
    abort(404, 'arguments not found')
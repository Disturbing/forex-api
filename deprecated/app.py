#!/usr/bin/python3
'''
Currency Converter API
'''
from datetime import datetime
from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from forex_python.converter import CurrencyRates, Decimal, RatesNotAvailableError

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
c = CurrencyRates()
rates = list(c.get_rates('').keys())


def check_date(dateC):
    """checks that date is valid and within the limit"""
    if dateC:
        try:
            dt = datetime.strptime(dateC, '%Y-%m-%d')
            if dt < datetime(1999, 1, 4) or dt > datetime.now():
                abort(400, 'date outside of range (1999-01-03-present)')
            return dt
        except ValueError:
            abort(400, 'invalid date')
    return None


def create_query(dicts, dt=None):
    """"creates query dict based on valid request args only"""
    query = {}
    if dt:
        query['on'] = dt.strftime("%A, %B %d, %Y")
    _from = dicts.get('from')
    if not _from:
        abort(400, "missing field: from")
    query['from'] = _from.upper()
    _to = dicts.get('to')
    if not _to:
        abort(400, "missing field: to")
    query['to'] = _to.upper()
    return query


@app.errorhandler(404)
def page_not_found(e):
    '''
    custom 404 error
    '''
    msg = e.__dict__.get('description') or "Not Found"
    return jsonify({"error": msg}), 404


@app.errorhandler(400)
def bad_request(e):
    '''
    custom 400 error
    '''
    msg = e.__dict__.get('description') or "Bad Request"
    return jsonify({"error": msg}), 400


@app.route('/api/status', methods=['GET'])
def getStatus():
    """shows that api is up"""
    return jsonify({'status': 'OK'})


@app.route('/api/currencies', methods=['GET'])
def getCurrencies():
    """gets all possible currencies to query with"""
    return jsonify({"currency": rates})


@app.route('/api/get_rates/<currency>', methods=['GET'])
@app.route('/api/get_rates', methods=['GET'])
def getRate(currency=None):
    '''
    Gets rates based on target currency

    Parameters (optional)
    ----------
    currency: string
        a currency to set target against all other currencies
    on: date, YYYY-MM-DD
        find rates based on a specific date
    from: string
        first rate to compare to
    to: string
        second rate to compare against first
    None: no arguments given
        Default target currency is used, 'USD'
    Returns
    -------
    JSON of results based on parameters
    '''
    dt = check_date(request.args.get('on'))
    query = {}
    if not dt:
        query['timestamp'] = str(datetime.now())
    if currency:
        try:
            query['target'] = currency.upper()
            if dt:
                query['on'] = dt.strftime("%A, %B %d, %Y")
            query['rates'] = c.get_rates(currency.upper(), dt)
            return jsonify(query)
        except RatesNotAvailableError:
            abort(400, 'invalid rate')
        except BaseException:
            abort(404)
    elif request.args:
        query = create_query(request.args, dt)
        try:
            query['rate'] = c.get_rate(query['from'],
                                       query['to'], dt)
            return jsonify(query)
        except BaseException:
            abort(400, 'invalid arguments')
    else:
        query['default'] = 'USD'
        query['rates'] = c.get_rates('USD')
        return jsonify(query)


@app.route('/api/convert', methods=['GET'])
def getConversion():
    '''
    returns converted amount based on parameters

    Parameters
    ----------
    (optional) on: date, YYYY-MM-DD
        find rates based on a specific date
    from: string
        currency to convert from
    to: string
        currency to convert to
    amt: int
        amount of currency
    Returns
    -------
    JSON of query, results, and additional info
    '''
    query = {}
    dt = check_date(request.args.get('on'))
    if request.args:
        query = create_query(request.args, dt)
        _amt = request.args.get('amt')
        if not _amt:
            abort(400, "missing field: amt")
        query['amt'] = _amt
        try:
            result = c.convert(query['from'], query['to'], Decimal(_amt), dt)
            info = {"rate": c.get_rate(query['from'], query['to'], dt)}
            if not dt:
                info['timestamp'] = str(datetime.now())
            return jsonify({"query": query,
                            "info": info, "result": result})
        except BaseException:
            abort(400, 'invalid arguments')
    abort(404, 'arguments not found')


if __name__ == "__main__":
    apiHost = "0.0.0.0"
    apiPort = 5000
    app.run(host=apiHost, port=int(apiPort), threaded=True)

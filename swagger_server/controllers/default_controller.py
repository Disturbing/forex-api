import connexion
import six

from swagger_server.models.conversion import Conversion  # noqa: E501
from swagger_server.models.conversions import Conversions  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.iso4217s import ISO4217s  # noqa: E501
from swagger_server import util

from forex_python.converter import CurrencyRates, RatesNotAvailableError
from datetime import datetime

# get a list of all currencies to check for errors
c = CurrencyRates()
all_curs = ["AUD"]
for cur in c.get_rates("AUD"):
    all_curs.append(cur)

# Set the appropriate format string for parsing dates
date_format = "%Y-%m-%d"

def get_available_currencies():  # noqa: E501
    """Get an array of available currencies

    Gets an array of the 3 letter ISO 4217 alphabetic codes for all available currencies. # noqa: E501


    :rtype: ISO4217s
    """
    return ISO4217s(all_curs), 200


def get_convert_frm_to_amt(frm, to, amt, date=None):  # noqa: E501
    """gives converted amount based on parameters

    returns a Conversion object based on parameters # noqa: E501

    :param _frm: Three letter ISO 4217 alphabetic code for the currency thats being converted from.
    :type _frm: str
    :param to: Three letter ISO 4217 alphabetic code for the currency thats being converted to.
    :type to: str
    :param amt: The amount of base currency to convert from.
    :type amt: 
    :param date: YYYY-MM-DD format of date to check rates on
    :type date: str

    :rtype: Conversion
    """
    if frm not in all_curs:
        return Error("from parameter is not a supported ISO4217 alphabetic code", 404, "Not Supported", "about:blank"), 404
    if to not in all_curs:
        return Error("to parameter is not a supported ISO4217 alphabetic code", 404, "Not Supported", "about:blank"), 404

    if date is None:
        date = datetime.today().strftime(date_format)

    try:
        dt = datetime.strptime(date, date_format)
    except ValueError:
        return Error("invalid date, date format is YYYY-MM-DD", 404, "Invalid Date", "about:blank"), 404

    try:
        return Conversion(date, frm, to, amt, c.convert(frm, to, amt, dt)), 200
    except RatesNotAvailableError as e:
        return Error(str(e), 404, "Rates Not Available", "about:blank"), 404



def get_get_rate_frm_to(frm, to, date=None):  # noqa: E501
    """Gets rate from one currency to another.

    Returns a Conversion object with from_amt equal to 1. # noqa: E501

    :param _frm: Three letter ISO 4217 alphabetic code for the currency that&#39;s being converted from.
    :type _frm: str
    :param to: Three letter ISO 4217 alphabetic code for the currency that&#39;s being converted to.
    :type to: str
    :param date: YYYY-MM-DD format of date to check rates on
    :type date: str

    :rtype: Conversion
    """
    if frm not in all_curs:
        return Error("from parameter is not a supported ISO4217 alphabetic code", 404, "Not Supported", "about:blank"), 404
    if to not in all_curs:
        return Error("to parameter is not a supported ISO4217 alphabetic code", 404, "Not Supported", "about:blank"), 404

    if date is None:
        date = datetime.today().strftime(date_format)

    try:
        dt = datetime.strptime(date, date_format)
    except ValueError:
        return Error("invalid date, date format is YYYY-MM-DD", 404, "Invalid Date", "about:blank"), 404

    try:
        return Conversion(date, frm, to, 1.0, c.get_rate(frm, to, dt)), 200
    except RatesNotAvailableError as e:
        return Error(str(e), 404, "Rates Not Available", "about:blank"), 404


def get_get_rates_frm(frm, date=None):  # noqa: E501
    """Get all rates against a currency.

    Gets Array of Conversion of all available currencies against the base currency (from parameter). # noqa: E501

    :param _frm: Base currency to get rates against.
    :type _frm: str
    :param date: YYYY-MM-DD format of date to check rates on.
    :type date: str

    :rtype: Conversions
    """
    if frm not in all_curs:
        return Error("from parameter is not a supported ISO4217 alphabetic code", 404, "Not Supported", "about:blank"), 404

    if date is None:
        date = datetime.today().strftime(date_format)

    try:
        dt = datetime.strptime(date, date_format)
    except ValueError:
        return Error("invalid date, date format is YYYY-MM-DD", 404, "Invalid Date", "about:blank"), 404

    rates = []
    try:
        rates_dict = c.get_rates(frm, dt)
    except RatesNotAvailableError as e:
        return Error(str(e), 404, "Rates Not Available", "about:blank"), 404

    for cur, rate in rates_dict.items():
        rates.append(Conversion(date, frm, cur, 1.0, rate))

    return Conversions(rates), 200

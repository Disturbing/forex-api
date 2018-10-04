import connexion
import six

from swagger_server.models.conversion import Conversion  # noqa: E501
from swagger_server.models.conversions import Conversions  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.iso4217s import ISO4217s  # noqa: E501
from swagger_server import util

from forex_python.converter import CurrencyRates

def get_available_currencies():  # noqa: E501
    """Get an array of available currencies

    Gets an array of the 3 letter ISO 4217 alphabetic codes for all available currencies. # noqa: E501


    :rtype: ISO4217s
    """
    all_curs = ["AUD"]
    c = CurrencyRates()
    for cur in c.get_rates('AUD'):
        all_curs.append(cur)
    return ISO4217s(all_curs)


def get_convert_from_to_amt(_from, to, amt, date=None):  # noqa: E501
    """gives converted amount based on parameters

    returns a Conversion object based on parameters # noqa: E501

    :param _from: Three letter ISO 4217 alphabetic code for the currency thats being converted from.
    :type _from: str
    :param to: Three letter ISO 4217 alphabetic code for the currency thats being converted to.
    :type to: str
    :param amt: The amount of base currency to convert from.
    :type amt: 
    :param date: YYYY-MM-DD format of date to check rates on
    :type date: str

    :rtype: Conversion
    """
    return 'do some magic!'


def get_get_rate_from_to(_from, to, date=None):  # noqa: E501
    """Gets rate from one currency to another.

    Returns a Conversion object with from_amt equal to 1. # noqa: E501

    :param _from: Three letter ISO 4217 alphabetic code for the currency that&#39;s being converted from.
    :type _from: str
    :param to: Three letter ISO 4217 alphabetic code for the currency that&#39;s being converted to.
    :type to: str
    :param date: YYYY-MM-DD format of date to check rates on
    :type date: str

    :rtype: Conversion
    """
    return 'do some magic!'


def get_get_rates_from(_from, date=None):  # noqa: E501
    """Get all rates against a currency.

    Gets Array of Conversion of all available currencies against the base currency (from parameter). # noqa: E501

    :param _from: Base currency to get rates against.
    :type _from: str
    :param date: YYYY-MM-DD format of date to check rates on.
    :type date: str

    :rtype: Conversions
    """
    return 'do some magic!'

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.conversion import Conversion  # noqa: E501
from swagger_server.models.conversions import Conversions  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.iso4217s import ISO4217s  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_convert_get(self):
        """Test case for convert_get

        gives converted amount based on parameters
        """
        query_string = [('date', 'current date')]
        response = self.client.open(
            '/Dkazem91/KintoHubCurrencies/1/convert/{from}/{to}/{amt}'.format(_from='_from_example', to='to_example', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_currencies_get(self):
        """Test case for currencies_get

        Get an array of available currencies
        """
        response = self.client.open(
            '/Dkazem91/KintoHubCurrencies/1/available_currencies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rate_get(self):
        """Test case for get_rate_get

        Gets rate from one currency to another.
        """
        query_string = [('date', 'current date')]
        response = self.client.open(
            '/Dkazem91/KintoHubCurrencies/1/get_rate/{from}/{to}'.format(_from='_from_example', to='to_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rates_get(self):
        """Test case for get_rates_get

        Get all rates against a currency.
        """
        query_string = [('date', 'current date')]
        response = self.client.open(
            '/Dkazem91/KintoHubCurrencies/1/get_rates/{from}'.format(_from='_from_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

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

    def test_get_available_currencies(self):
        """Test case for get_available_currencies

        Get an array of available currencies
        """
        response = self.client.open(
            '/forex/available_currencies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        query_string = [('date', 'current date')]
        response = self.client.open(
            '/forex/convert/{from}/{to}/{amt}'.format(_frm='_frm_example', to='to_example', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to(self):
        """Test case for get_get_rate_frm_to

        Gets rate from one currency to another.
        """
        query_string = [('date', 'current date')]
        response = self.client.open(
            '/forex/get_rate/{from}/{to}'.format(_frm='_frm_example', to='to_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rates_frm(self):
        """Test case for get_get_rates_frm

        Get all rates against a currency.
        """
        query_string = [('date', 'current date')]
        response = self.client.open(
            '/forex/get_rates/{from}'.format(_frm='_frm_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

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

    def test_get_convert_frm_to_amt_with_date(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        query_string = [('date', '2018-04-10')]
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_no_date(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_date(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        query_string = [('date', '2018-13-10')]
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_frm(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='UUUUUUUU', to='CAD', amt=8.14),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_to(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='DDDDDDDDDDDD', amt=8.14),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_amt(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt='abc123'),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_negative_amt(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=-8.14),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_no_date_data(self):
        """Test case for get_convert_frm_to_amt

        gives converted amount based on parameters
        """
        query_string = [('date', '1995-04-10')]
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # def test_get_get_rate_frm_to(self):
    #     """Test case for get_get_rate_frm_to

    #     Gets rate from one currency to another.
    #     """
    #     query_string = [('date', 'current date')]
    #     response = self.client.open(
    #         '/forex/get_rate/{frm}/{to}'.format(frm='_frm_example', to='to_example'),
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    # def test_get_get_rates_frm(self):
    #     """Test case for get_get_rates_frm

    #     Get all rates against a currency.
    #     """
    #     query_string = [('date', 'current date')]
    #     response = self.client.open(
    #         '/forex/get_rates/{frm}'.format(frm='_frm_example'),
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

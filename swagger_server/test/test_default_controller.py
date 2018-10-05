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
        response = self.client.open(
            '/forex/available_currencies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_with_date(self):
        query_string = [('date', '2018-04-10')]
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_no_date(self):
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_date(self):
        query_string = [('date', '2018-13-10')]
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_frm(self):
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='UUUUUUUU', to='CAD', amt=8.14),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_to(self):
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='DDDDDDDDDDDD', amt=8.14),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_bad_amt(self):
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt='abc123'),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_negative_amt(self):
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=-8.14),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_convert_frm_to_amt_no_date_data(self):
        query_string = [('date', '1995-04-10')]
        response = self.client.open(
            '/forex/convert/{frm}/{to}/{amt}'.format(frm='USD', to='CAD', amt=8.14),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to_with_date(self):
        query_string = [('date', '2018-10-04')]
        response = self.client.open(
            '/forex/get_rate/{frm}/{to}'.format(frm='USD', to='CAD'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to_bad_date(self):
        query_string = [('date', '2018-13-04')]
        response = self.client.open(
            '/forex/get_rate/{frm}/{to}'.format(frm='USD', to='CAD'),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to_bad_frm(self):
        response = self.client.open(
            '/forex/get_rate/{frm}/{to}'.format(frm='USSSS', to='CAD'),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to_bad_to(self):
        response = self.client.open(
            '/forex/get_rate/{frm}/{to}'.format(frm='USD', to='CADDDD'),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to_no_date_data(self):
        query_string = [('date', '1995-04-10')]
        response = self.client.open(
            '/forex/get_rate/{frm}/{to}'.format(frm='USD', to='CAD'),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rate_frm_to_no_date(self):
        response = self.client.open(
            '/forex/get_rate/{frm}/{to}'.format(frm='USD', to='CAD'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rates_frm_with_date(self):
        query_string = [('date', '2018-10-04')]
        response = self.client.open(
            '/forex/get_rates/{frm}'.format(frm='USD'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rates_frm_bad_date(self):
        query_string = [('date', '2018-13-04')]
        response = self.client.open(
            '/forex/get_rates/{frm}'.format(frm='USD'),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rates_frm_bad_frm(self):
        query_string = [('date', '2018-10-04')]
        response = self.client.open(
            '/forex/get_rates/{frm}'.format(frm='USDDDD'),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rates_frm_no_date_data(self):
        query_string = [('date', '1995-04-10')]
        response = self.client.open(
            '/forex/get_rates/{frm}'.format(frm='USD'),
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_get_rates_frm_no_date(self):
        response = self.client.open(
            '/forex/get_rates/{frm}'.format(frm='USD'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()



#!/usr/bin/env python3
"""module docs for side_effects.py"""
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests module to control its behavior
requests = Mock()


def get_holidays():
    '''dummy function'''
    req = requests.get('http://it-doesnt matter.bye')

    # print(r.status_code) # this gives a random mock object
    if req.status_code == 200:  # if request was successful
        return req.json()
    return None


class TestCalendar(unittest.TestCase):
    '''class test the function'''

    def test_get_holidays_timeout(self):
        '''Test a request's connection timeout'''
        # use the request.Timeout class
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    def test_get_holidays_exceptions(self):
        '''similarly we can mock any oda exceptions'''
        requests.get.side_effect = IndexError
        with self.assertRaises(IndexError):
            get_holidays()

    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '10/1': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        ret_val = get_holidays()
        assert ret_val['12/25'] == 'Christmas'
        assert ret_val['10/1'] == 'Independence Day'


if __name__ == "__main__":
    unittest.main()

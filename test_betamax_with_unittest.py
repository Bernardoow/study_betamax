import betamax
from betamax.fixtures import unittest
import requests

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'bernardo'


def function():
    response = requests.get('https://httpbin.org/get')
    return response.json().get('url')


class IntegrationTestCase(unittest.BetamaxTestCase):
    # CASSETTE_LIBRARY_DIR = "./bernardo"
    pass


class SpecificTestCase(IntegrationTestCase):
    def test_something(self):
        self.assertEqual(function(), 'https://httpbin.org/get')

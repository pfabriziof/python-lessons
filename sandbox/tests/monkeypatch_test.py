import requests
from src import functions
from pathlib import Path

def test_getssh(monkeypatch):
    # mocked return to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path('/abc')

    monkeypatch.setattr(Path, 'home', mockreturn)

    x = functions.getssh()
    assert x == Path('/abc/.ssh')


# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    @staticmethod
    # mock json() always returns a specific testing dictionary
    def json():
        return {"mock_key": "mock_response"}

def test_get_json(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    result = functions.get_json('https://fakeurl')
    assert result['mock_key'] == 'mock_response'


import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    response = requests.get(url)
    body = response.json()

    print(body)
    assert response.status_code == 200
    assert 'Wikipedia' in body['AbstractSource']

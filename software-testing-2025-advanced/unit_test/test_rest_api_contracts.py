
import pytest
import requests
from jsonschema import validate

JSONPLACEHOLDER = 'https://jsonplaceholder.typicode.com'
HTTPBIN = 'https://httpbin.org'

post_schema = {
    'type': 'object',
    'properties': {
        'userId': {'type': 'integer'},
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
    },
    'required': ['userId', 'id', 'title', 'body'],
}

def test_posts_list_contract():
    resp = requests.get(f'{JSONPLACEHOLDER}/posts', timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list) and len(data) > 0
    validate(instance=data[0], schema=post_schema)

@pytest.mark.parametrize('post_id', [1, 50, 100])
def test_post_detail_contract(post_id):
    resp = requests.get(f'{JSONPLACEHOLDER}/posts/{post_id}', timeout=10)
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=post_schema)

def test_httpbin_404_negative():
    r = requests.get(f'{HTTPBIN}/status/404', timeout=10)
    assert r.status_code == 404

import time
import pytest
import requests
from jsonschema import validate
from requests.exceptions import RequestException

JSONPLACEHOLDER = 'https://jsonplaceholder.typicode.com'
HTTPBIN = 'https://httpbin.org'

# JSON 契约
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


def _get(url, **kw):
    """简单重试 3 次；三次都失败就跳过，避免云端网络抖动导致 CI 挂掉。"""
    for i in range(3):
        try:
            # 设置更长的超时时间，确保 API 请求有足够时间响应
            return requests.get(url, timeout=30, **kw)  # 增加超时时间
        except RequestException as e:
            if i == 2:
                pytest.skip(f"network unstable, skip test: {e}")
            time.sleep(2)  # 延长重试间隔，以防过快请求导致失败


def test_posts_list_contract():
    resp = _get(f'{JSONPLACEHOLDER}/posts')
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list) and len(data) > 0
    validate(instance=data[0], schema=post_schema)


@pytest.mark.parametrize('post_id', [1, 50, 100])
def test_post_detail_contract(post_id):
    resp = _get(f'{JSONPLACEHOLDER}/posts/{post_id}')
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=post_schema)


def test_httpbin_404_negative():
    r = _get(f'{HTTPBIN}/status/404')
    assert r.status_code == 404

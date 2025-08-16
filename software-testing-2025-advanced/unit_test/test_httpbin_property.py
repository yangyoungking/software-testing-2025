import string
from hypothesis import given, settings, strategies as st
import requests

HTTPBIN = 'https://httpbin.org'


@settings(deadline=None, max_examples=15)
@given(
    q=st.text(alphabet=string.ascii_letters +
              string.digits, min_size=0, max_size=10),
    page=st.integers(min_value=0, max_value=999)
)
def test_httpbin_query_roundtrip(q, page):
    params = {'q': q, 'page': str(page)}
    try:
        resp = requests.get(
            f'{HTTPBIN}/get', params=params, timeout=30)  # 增加超时设置
        assert resp.status_code == 200
        data = resp.json()
        assert data['args'] == {'q': q, 'page': str(page)}
    except requests.RequestException as e:
        pytest.skip(f"Request failed: {e}")

import pytest
import requests 

from core.config import BASE_URL,TIMEOUT

@pytest.mark.smoke
@pytest.mark.regression
def test_health_returns_ok():
    r = requests.get(f"{BASE_URL}/health",timeout = TIMEOUT)
    assert r.status_code == 200
    j = r.json()
    assert j.get("status") == "ok"


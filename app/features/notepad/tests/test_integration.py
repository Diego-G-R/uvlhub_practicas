"""HTTP integration tests for the notepad feature.

Drive the application through the Flask test client. The ``test_client``
fixture from splent_framework rebuilds a clean DB per test for full isolation.
"""
import pytest

pytestmark = pytest.mark.integration


def test_notepad_index_requires_login(test_client):
    response = test_client.get("/notepad", follow_redirects=False)
    assert response.status_code in (302, 303)
    assert "/login" in response.headers["Location"]

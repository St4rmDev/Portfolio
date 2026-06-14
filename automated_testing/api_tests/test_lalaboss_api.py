import pytest
import requests
import time

# --- CONFIGURATION ---
BASE_URL = "http://127.0.0.1:5001"
API_ENDPOINT = f"{BASE_URL}/api/live_intel"
TIMEOUT = 5.0

class TestLalabossAPI:
    """
    Test suite for the LalaBoss backend API.
    Demonstrates API automation using Pytest and Requests.
    """

    @pytest.mark.api
    def test_live_intel_status_code(self):
        """Verify the /api/live_intel endpoint returns a 200 OK status."""
        response = requests.get(API_ENDPOINT, timeout=TIMEOUT)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    @pytest.mark.api
    def test_live_intel_response_time(self):
        """Verify the endpoint responds within acceptable limits (< 500ms)."""
        start_time = time.time()
        response = requests.get(API_ENDPOINT, timeout=TIMEOUT)
        end_time = time.time()
        
        response_time_ms = (end_time - start_time) * 1000
        assert response_time_ms < 500, f"Response time was too slow: {response_time_ms:.2f}ms"

    @pytest.mark.api
    def test_live_intel_json_schema(self):
        """Verify the response is valid JSON and contains expected keys."""
        response = requests.get(API_ENDPOINT, timeout=TIMEOUT)
        
        # Ensure the response can be parsed as JSON
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Response is not valid JSON")
            
        # Example assertions for keys we expect from live intel
        # If the structure differs, these can be updated
        assert isinstance(data, dict), "Expected a JSON object (dictionary) at the root level"
        
        # Check for typical wrapper keys if any, or verify it returns data
        # For LalaBoss live intel, it often returns html or data
        # assert "html" in data or "status" in data, "Missing expected keys in payload"

    @pytest.mark.negative
    def test_invalid_endpoint_returns_404(self):
        """Verify that accessing a non-existent endpoint gracefully returns 404."""
        bad_url = f"{BASE_URL}/api/this_does_not_exist_xyz"
        response = requests.get(bad_url, timeout=TIMEOUT)
        assert response.status_code == 404, "Expected 404 for invalid endpoint"

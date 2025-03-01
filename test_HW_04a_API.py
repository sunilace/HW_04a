import json
from HW_04a_API import details
from unittest.mock import patch
mocked_commit_data = json.dumps([{"comments_url": "dummy_url"}] * 10)
mocked_repos_data = json.dumps([
    {"name": "csp"},
    {"name": "hellogitworld"},
    {"name": "helloworld"},
    {"name": "Mocks"},
    {"name": "Project1"},
    {"name": "richkempinski.github.io"},
    {"name": "threads-of-life"},
    {"name": "try_nbdev"},
    {"name": "try_nbdev2"},
])

@patch("requests.get")  # Mock requests.get globally in this test function
def test_status_code_404_invalid_id(mock_get):
    mock_get.return_value.status_code = 404
    assert details("Invalid_Github_Id") == "Status Code: 404"

@patch("requests.get")
def test_working_API_Example(mock_get):
    def mock_requests_get(url, *args, **kwargs):
        if "repos" in url and "users" in url:
            mock_response = patch("requests.Response")
            mock_response.status_code = 200
            mock_response.text = mocked_repos_data
            return mock_response
        elif "commits" in url:
            mock_response = patch("requests.Response")
            mock_response.status_code = 200
            mock_response.text = mocked_commit_data
            return mock_response
        else:
            mock_response = patch("requests.Response")
            mock_response.status_code = 404
            return mock_response

    mock_get.side_effect = mock_requests_get
    expected_data = """Repository name: csp, Commits: 10
Repository name: hellogitworld, Commits: 10
Repository name: helloworld, Commits: 10
Repository name: Mocks, Commits: 10
Repository name: Project1, Commits: 10
Repository name: richkempinski.github.io, Commits: 10
Repository name: threads-of-life, Commits: 10
Repository name: try_nbdev, Commits: 10
Repository name: try_nbdev2, Commits: 10
"""
    assert details("richkempinski") == expected_data

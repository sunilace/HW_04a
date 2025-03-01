from HW_04a_API import details
from unittest.mock import Mock, patch


@patch(HW_04a_API.details)
def test_status_code_404_invalid_id(mock_get):
    mock_get.return_value = "Status Code: 404"
    assert details("Invalid_Github_Id") == "Status Code: 404"


@patch(HW_04a_API.details)
def test_working_API_Example(mock_get):
    mock_get.return_value = """Repository name: csp, Commits: 2
Repository name: hellogitworld, Commits: 50
Repository name: helloworld, Commits: 6
Repository name: Mocks, Commits: 10
Repository name: Project1, Commits: 2
Repository name: richkempinski.github.io, Commits: 9
Repository name: threads-of-life, Commits: 1
Repository name: try_nbdev, Commits: 2
Repository name: try_nbdev2, Commits: 5
"""
    data = """Repository name: csp, Commits: 2
Repository name: hellogitworld, Commits: 50
Repository name: helloworld, Commits: 6
Repository name: Mocks, Commits: 10
Repository name: Project1, Commits: 2
Repository name: richkempinski.github.io, Commits: 9
Repository name: threads-of-life, Commits: 1
Repository name: try_nbdev, Commits: 2
Repository name: try_nbdev2, Commits: 5
"""
    assert details("richkempinski") == data

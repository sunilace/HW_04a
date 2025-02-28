from HW_04a_API import details


def test_status_code_404_invalid_id():
    assert details("Invalid_Github_Id") == "Status Code: 404"


def test_working_API_Example():
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

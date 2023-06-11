import pytest


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


def pytest_addoption(parser):
    parser.addoption("--user",
                     action="store",
                     default='',
                     type=str,
                     required=True,
                     help="Set user number")
    parser.addoption("--password",
                     action="store",
                     default='',
                     type=str,
                     required=True,
                     help="Set password")


@pytest.fixture(scope="session")
def user(request):
    return request.config.getoption("--user")


@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")

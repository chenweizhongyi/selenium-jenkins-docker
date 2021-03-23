import pytest


@pytest.fixture(scope="module",autouse=True)
def login():
    print('登录')
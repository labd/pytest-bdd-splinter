from multiprocessing import Process

import pytest

from pytest_bdd_splinter import *  # noqa


@pytest.fixture(scope="session")
def browser_base_url():
    return "http://localhost:5000"


@pytest.fixture(scope="session", autouse=True)
def run_serv(request):
    from .server import app

    server = Process(target=app.run, kwargs={"debug": False})
    server.start()

    def stop():
        server.terminate()
        server.join()

    request.addfinalizer(stop)

import pytest
import structlog

from webdrivery.webdrivery import WebDrivery, Settings
from webdrivery.tests import yandex

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ],
)


@pytest.fixture(scope='session', autouse=True)
def init_browser(request):
    s = Settings(
        host='http://ya.ru',
        headless=False,
        browser_name='chrome'
    )
    y = WebDrivery()
    y.init_browser(s)

    def quit_browser():
        y.quit_browser()

    request.addfinalizer(quit_browser)


@pytest.fixture(autouse=True)
def open_yandex():
    yandex.open()

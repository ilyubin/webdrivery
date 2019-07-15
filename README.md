# WebDrivery #


## Introduction

Python + Webdriver + StructLog

## Setup ##

Initialize `WebDrivery` in `conftest.py`.

```python
import pytest
from webdrivery.webdrivery import WebDrivery, Settings


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
```

You can create follow `Settings`, if not it use values by default:
```python
host: str, # required
browser_name: str = 'chrome',
headless: bool = True,
incognito: bool = True,
implicit_wait: int = 4,
timeout_wait: int = 4,
highlight_style: str = 'outline: 2px dashed red',
highlight_timeout: float = 0.4,
type_slow_pause: float = 0.3,
window_width: int = 1440,
window_height: int = 900,
window_position_x: int = 0,
window_position_y: int = 0,
mobile_device_name: str = '',
user_agent: str = '',
command_executor: str = '',
capabilities: dict = None,
event_listener: AbstractEventListener = None,
```

## Usage ##

Create module with your step-methods.

```python
# yandex.py
from selenium.webdriver.common.by import By
from webdrivery import action


def open():
    action.open_page_by_path('')


def search_by_text(query):
    action.type((By.ID, 'text'), query)
    action.click((By.CSS_SELECTOR, '.button_theme_websearch'))
```

Define your methods as many as you need. Then use methods in tests:

```python
# test_yandex.py
from webdrivery.tests import yandex


def test_search_yandex():
    yandex.open()
    yandex.search_by_text('python')
    ...
```

Add more actions and asserts.

## Locators ##

Put locators in actions as `tuple` in this `()` brackets:

```python
(By.ID, 'text')
(By.CSS_SELECTOR, '.button_theme_websearch')
```

In most cases preferable to use `ID` or `CSS_SELECTOR` locator's types.

##  Available actions ##

Url actions
* `open_url`
* `open_relative_path`
* `get_current_url`

Page actions
* `back`
* `in_iframe`
* `refresh_page`

General actions
* `clear`
* `clear_and_send_keys`
* `click`
* `find_element`
* `find_elements`
* `send_keys`
* `send_keys_slowly`

Select actions:
* `select_by_index`
* `select_by_value`
* `select_by_visible_text`

Get actions
* `count_elements`
* `get_attribute_by_name`
* `get_css_property`
* `get_element_text`
* `get_elements_text`
* `get_element_value`
* `get_title`

Bool actions
* `is_element_displayed`
* `is_element_enabled`

Wait actions
* `wait_document_ready_state_complete`
* `wait_for_element_visible`
* `wait_for_element_disappear`
* `wait_for_url_changed`

Scroll actions
* `move_to_element`
* `scroll_to_bottom`
* `scroll_to_element`
* `scroll_to_top`

Javascript actions
* `execute_script`

Cookies
* `add_cookie`
* `delete_all_cookies`
* `delete_cookie_by_name`
* `get_cookies`

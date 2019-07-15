import structlog
import time
import types

from typing import Iterable
from urllib.parse import urljoin

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from webdrivery.webdrivery import WebDrivery

log = structlog.get_logger()


def open_url(url: str):
    log.debug('open_url', url=url)
    driver().get(url)


def open_relative_path(path: str):
    url = urljoin(y().s.host, path)
    log.debug('open_relative_path', path=path, url=url)
    driver().get(url)


def refresh_page():
    log.debug('refresh_page')
    driver().refresh()


def back():
    log.debug('back')
    driver().back()


def get_current_url() -> str:
    url = driver().current_url
    log.debug('get_current_url', url=url)
    return url


def find_element(locator: tuple) -> WebElement:
    log.debug('find_element', by=locator)
    element = driver().find_element(*locator)
    _highlight(element)
    return element


def find_elements(locator: tuple) -> Iterable[WebElement]:
    log.debug('find_elements', by=locator)
    elements = driver().find_elements(*locator)
    _highlight_all(elements)
    return elements


# noinspection PyShadowingBuiltins
def send_keys(locator: tuple, text: str):
    log.debug('send_keys', by=locator, text=text)
    _find_element(locator).send_keys(text)


def send_keys_slowly(locator: tuple, text: str, pause: int = 0):
    pause = pause or y().s.type_slow_pause
    log.debug('send_keys_slowly', by=locator, text=text, pause=pause)
    element = _find_element(locator)
    element.clear()
    for t in text:
        element.send_keys(t)
        time.sleep(pause)


def clear(locator: tuple):
    log.debug('clear', by=locator)
    _find_element(locator).clear()


def clear_and_send_keys(locator: tuple, text: str):
    log.debug('clear_and_send_keys', by=locator, text=text)
    element = _find_element(locator)
    element.clear()
    element.send_keys(text)


def click(locator: tuple):
    log.debug('click', by=locator)
    _find_element(locator).click()


def select_by_index(locator: tuple, index: int):
    log.debug('select_by_index', by=locator, index=index)
    element = Select(_find_element(locator))
    element.select_by_index(index)


def select_by_value(locator: tuple, value: str):
    log.debug('select_by_value', by=locator, value=value)
    element = Select(_find_element(locator))
    element.select_by_value(value)


def select_by_visible_text(locator: tuple, text: str):
    log.debug('select_by_visible_text', by=locator, text=text)
    element = Select(_find_element(locator))
    element.select_by_visible_text(text)


def count_elements(locator: tuple) -> int:
    count = 0
    try:
        count = len(list(_find_elements(locator)))
    except NoSuchElementException:
        pass
    log.debug('count_elements', by=locator, count=count)
    return count


def get_element_text(locator: tuple) -> str:
    text = _find_element(locator).text
    log.debug('get_element_text', by=locator, text=text)
    return text


def get_elements_text(locator: tuple) -> Iterable[str]:
    texts = [element.text for element in _find_elements(locator)]
    log.debug('get_elements_text', by=locator, texts=texts)
    return texts


def get_attribute_by_name(locator: tuple, attribute_name: str) -> str:
    element = _find_element(locator)
    attribute_value = element.get_attribute(attribute_name)
    log.debug(
        'get_attribute_by_name',
        by=locator,
        attribute={
            'name': attribute_name,
            'value': attribute_value,
        },
    )
    return attribute_value


def get_css_property(locator: tuple, property_name: str) -> str:
    element = find_element(locator)
    value = element.value_of_css_property(property_name)
    log.debug(
        'get_css_property',
        by=locator,
        attribute={
            'name': property_name,
            'value': value,
        },
    )
    return value


def get_element_value(locator: tuple) -> str:
    element = _find_element(locator)
    value = element.get_attribute('value')
    log.debug('get_element_value', by=locator, value=value)
    return value


def get_title() -> str:
    title = driver().title
    log.debug('get_title', title=title)
    return title


def wait_for_element_visible(locator: tuple, timeout: int = 0):
    log.debug('wait_for_element_visible', by=locator, timeout=timeout)
    WebDriverWait(driver(), timeout or y().s.timeout_wait).until(
        lambda driver: driver.find_element(*locator).is_displayed())


def wait_for_element_disappear(locator: tuple, timeout: int = 0):
    log.debug('wait_for_element_disappear', by=locator, timeout=timeout)
    WebDriverWait(driver(), timeout or y().s.timeout_wait).until_not(
        lambda driver: driver.find_element(*locator).is_displayed())


def wait_document_ready_state_complete(timeout: int = 0):
    log.debug('wait_document_ready_state_complete', timeout=timeout)
    WebDriverWait(driver(), timeout or y().s.timeout_wait).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete')


def wait_for_url_changed(expected_url, timeout: int = 0):
    log.debug('wait_for_url_changed', expected_url=expected_url, timeout=timeout)
    WebDriverWait(driver(), timeout or y().s.timeout_wait).until(
        lambda: expected_url == get_current_url())


def is_element_displayed(locator: tuple) -> bool:
    try:
        is_displayed = _find_element(locator).is_displayed()
        log.debug('is_element_displayed', by=locator, is_displayed=is_displayed)
        return is_displayed
    except NoSuchElementException:
        return False


def is_element_enabled(locator: tuple) -> bool:
    is_enabled = _find_element(locator).is_enabled()
    log.debug('is_element_enabled', by=locator, is_enabled=is_enabled)
    return is_enabled


def scroll_to_element(locator: tuple):
    log.debug('scroll_to_element', by=locator)
    element = _find_element(locator)
    driver().execute_script('arguments[0].scrollIntoView(true);', element)


def scroll_to_top():
    log.debug('scroll_to_top')
    driver().execute_script('window.scrollTo(0, 0);')


def scroll_to_bottom():
    log.debug('scroll_to_bottom')
    driver().execute_script('window.scrollTo(0, document.body.scrollHeight);')


def move_to_element(locator: tuple):
    log.debug('move_to_element', by=locator)
    element = _find_element(locator)
    return ActionChains(driver()).move_to_element(element).perform()


def execute_script(script: str, *args):
    log.debug('execute_script', script=script, args=args)
    return driver().execute_script(script, *args)


def in_iframe(locator: tuple, action: types.LambdaType):
    log.debug('in_iframe', by=locator)
    driver().switch_to.frame(_find_element(locator))
    action()
    driver().switch_to.default_content()


def delete_all_cookies():
    log.debug('delete_all_cookies')
    driver().delete_all_cookies()


def add_cookie(cookie_dict: dict):
    log.debug('add_cookie', cookie_dict=cookie_dict)
    driver().add_cookie(cookie_dict)


def get_cookies() -> list:
    cookies = driver().get_cookies()
    log.debug('get_cookies', cookies=cookies)
    return cookies


def delete_cookie_by_name(cookie_name: str):
    log.debug('delete_cookie_by_name', cookie_name=cookie_name)
    driver().delete_cookie(cookie_name)


# Private methods ##################################################################################################

def y() -> WebDrivery:
    return WebDrivery()


def driver() -> WebDriver:
    return y().get_driver()


def _find_element(locator: tuple) -> WebElement:
    element = driver().find_element(*locator)
    _highlight(element)
    return element


def _find_elements(locator: tuple) -> Iterable[WebElement]:
    elements = driver().find_elements(*locator)
    _highlight_all(elements)
    return elements


def _highlight(element: WebElement):
    _set_style_element(element, y().s.highlight_style)
    time.sleep(y().s.highlight_timeout)
    _set_style_element(element, '')


def _highlight_all(elements: list):
    _set_style_elements(elements, y().s.highlight_style)
    time.sleep(y().s.highlight_timeout)
    _set_style_elements(elements, '')


def _set_style_element(element: WebElement, style: str):
    driver().execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)


def _set_style_elements(elements: list, style: str):
    for element in elements:
        _set_style_element(element, style)

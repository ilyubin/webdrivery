import uuid

from hamcrest import equal_to, assert_that, empty
from selenium.webdriver.common.by import By

from webdrivery import action


class TestAction:

    def test_action_refresh_and_get_current_url(self):
        url = action.get_current_url()
        action.refresh_page()
        url2 = action.get_current_url()
        assert_that(url2, equal_to(url))

    def test_clear(self):
        textField = (By.ID, 'text')
        text = f'text-{uuid.uuid4()}'

        action.send_keys(textField, text)
        assert_that(action.get_element_value(textField), equal_to(text))

        action.clear(textField)
        assert_that(action.get_element_value(textField), empty())

    def test_clear_and_type(self):
        textField = (By.ID, 'text')
        text = f'text-{uuid.uuid4()}'

        action.clear_and_send_keys(textField, text)
        assert_that(action.get_element_value(textField), equal_to(text))

        new_text = f'new_text-{uuid.uuid4()}'
        action.clear_and_send_keys(textField, new_text)
        assert_that(action.get_element_value(textField), equal_to(new_text))

    def test_type(self):
        textField = (By.ID, 'text')
        text = f'text-{uuid.uuid4()}'

        action.send_keys(textField, text)
        assert_that(action.get_element_value(textField), equal_to(text))

        new_text = f'new_text-{uuid.uuid4()}'
        action.send_keys(textField, new_text)
        assert_that(action.get_element_value(textField), equal_to(text + new_text))

    def test_get_title(self):
        title = action.get_title()
        assert_that(title, equal_to('Яндекс'))

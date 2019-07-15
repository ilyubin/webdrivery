import uuid

from hamcrest import assert_that, empty, is_not, has_item, has_entries

from webdrivery import action


class TestCookies:

    def test_delete_all_cookies(self):
        action.delete_all_cookies()
        assert_that(action.get_cookies(), empty())

    def test_add_cookie(self):
        action.delete_all_cookies()
        cookie1 = {'name': 'a', 'value': 'x', 'path': '/'}
        cookie2 = {'name': 'b', 'value': 'y', 'path': '/'}
        action.add_cookie(cookie1)
        action.add_cookie(cookie2)
        cookies = action.get_cookies()
        assert_that(cookies, is_not(empty()))
        assert_that(cookies, has_item(has_entries(cookie1)))
        assert_that(cookies, has_item(has_entries(cookie2)))

    def test_delete_cookie_by_name(self):
        action.delete_all_cookies()
        cookie = {'name': f'name-{uuid.uuid4()}', 'value': f'value-{uuid.uuid4()}', 'path': '/'}
        action.add_cookie(cookie)
        assert_that(action.get_cookies(), has_item(has_entries(cookie)))
        action.delete_cookie_by_name(cookie['name'])
        assert_that(action.get_cookies(), is_not(has_item(has_entries(cookie))))

from hamcrest import assert_that, contains_string

from webdrivery.tests import yandex


class TestSearchYandex:

    def test_search_yandex(self):
        yandex.search_by_text('python')
        assert_that(yandex.has_search_results())
        assert_that(yandex.headers()[0].lower(), contains_string('python'))

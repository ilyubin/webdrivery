from selenium.webdriver.common.by import By

from webdrivery import action


def open():
    action.open_relative_path('')


def search_by_text(query):
    action.send_keys((By.ID, 'text'), query)
    action.click((By.CSS_SELECTOR, '.button_theme_websearch'))


def has_search_results():
    return action.is_element_displayed((By.CSS_SELECTOR, '.main__content .serp-list[role=main]'))


def headers():
    return action.get_elements_text((By.CSS_SELECTOR, 'li[data-cid] h2 [class$=text]'))

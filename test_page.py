import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.nondestructive
def test_page(page):
    """

    :type page: conftest.Page
    """
    page.go("/")
    page.hasTitle("Vacation Rentals, Homes, Experiences & Places - Airbnb")

    bar_items = page.multi_el("_lvb55za", By.CLASS_NAME)
    assert len(bar_items) == 5

    menu_names = ['Become a host', 'Earn credit', 'Help', 'Sign up', 'Log in']

    for i in bar_items:
        assert i.text == menu_names[bar_items.index(i)]

    bar_items[4].click()
    page.el("_wpwi48", By.CLASS_NAME)

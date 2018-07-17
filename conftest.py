from urllib.parse import urljoin

from pytest import fixture, yield_fixture
from pytest_selenium import SUPPORTED_DRIVERS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, invisibility_of_element_located, \
    title_contains
from selenium.webdriver.support.wait import WebDriverWait


@fixture(scope="module", name='page')
def selenium_page(request, base_url):
    driver_class = SUPPORTED_DRIVERS[request.config.getoption('driver')]
    driver = driver_class()
    yield Page(driver=driver, base_url=base_url)
    driver.quit()


class Page(object):

    TIMEOUT = 5

    def __init__(self, base_url, driver):
        self.base_url = base_url
        self.driver = driver

    @property
    def wait(self):
        return WebDriverWait(self.driver, self.TIMEOUT)

    # def wait_until_loaded(self):
    #     self.wait.until(title_contains("Vacation Rentals, Homes, Experiences & Places - Airbnb"))

    def go(self, path):
        self.driver.get(urljoin(self.base_url, path))
        # self.wait_until_loaded()

    def hasTitle(self, title):
        assert self.driver.title == title

    def el(self, locator, locator_type=By.CSS_SELECTOR, wait_for=element_to_be_clickable):
        return self.wait.until(wait_for((
            locator_type,
            locator
        )))

    def multi_el(self, locator, locator_type=By.CSS_SELECTOR, wait_for=element_to_be_clickable):
        self.wait.until(wait_for((locator_type, locator)))
        return self.driver.find_elements(locator_type, locator)
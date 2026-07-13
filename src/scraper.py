from collections.abc import Callable

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located,
    presence_of_element_located,
    staleness_of,
)
from selenium.webdriver.support.wait import WebDriverWait


class Scraper:
    def __init__(self, driver: WebDriver, url: str | None = None):
        self.driver = driver
        if url:
            self.driver.get(url)

    def _wait(
            self,
            element: WebDriver | WebElement | None = None,
            timeout: float = 2
    ) -> WebDriverWait:
        if element is None:
            element = self.driver
        return WebDriverWait(element, timeout=timeout)

    def _wait_find(
            self,
            path: str,
            element: WebDriver | WebElement | None = None,
            find_all: bool = False,
            timeout: float = 2
    ) -> WebElement | list[WebElement]:
        if element is None:
            element = self.driver
        if find_all:
            return self._wait(element, timeout=timeout).until(presence_of_all_elements_located((By.XPATH, path)))
        else:
            return self._wait(element, timeout=timeout).until(presence_of_element_located((By.XPATH, path)))

    def _wait_for_staleness(
            self,
            element: WebDriver | WebElement | None = None,
            timeout: float = 2
    ):
        if element is None:
            element = self.driver
        self._wait(timeout=timeout).until(staleness_of(element))

    def _wait_for_condition(
            self,
            condition_function: Callable,
            timeout: float = 2
    ):
        self._wait(timeout=timeout).until(condition_function)

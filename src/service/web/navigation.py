from RPA.Robocorp.WorkItems import WorkItems
from src.util.web import WebNavigationUtils
from src import Selenium
from time import sleep

class WebNavigation:
    def __init__(self, browser_instance: Selenium) -> None:
        self._browser = browser_instance
        self._work_item = WorkItems().get_input_work_item().payload

    def __search_phrase(self) -> None:
        WebNavigationUtils.input_text(browser_instance=self._browser, webelement_locator='class:search-page-input', text_to_input=self._work_item['searchPhrase'])
        sleep(5)
        # print(search_button)
        # WebNavigationUtils.click_element(browser_instance=self._browser, webelement_locator=search_button)

    def run(self) -> None:
        self.__search_phrase()


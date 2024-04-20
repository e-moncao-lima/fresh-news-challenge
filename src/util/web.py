from robocorp import storage, log
from typing import Optional
from RPA.Browser.Selenium import Selenium, WebElement, ElementNotFound


class WebAccessUtils:
    @staticmethod
    def setup_browser() -> Selenium:
        """Create a browser instance for web navigation

        Returns:
            Selenium: Web browser instance.
        """
        return Selenium()
    
    @staticmethod
    def get_web_locator(element_locator: str) -> Optional[str]:
        """Get web element locator from locator.json file from robocorp

        Args:
            element_locator (str): Web element as key in json file.

        Returns:
            Optional[str]: The web element locator string. Returns None if not found.
        """
        try:
            locators = storage.get_json('locators')
            return locators[element_locator]
        except Exception as error:
            log.exception(f"Error when trying to retrieve web locator: [{type(error).__name__}] {error}")

    @staticmethod
    def access_webpage(browser_instance: Selenium, webpage_url: str) -> None:
        """Access a webpage through its URL.

        Args:
            browser_instance (Selenium): Browser instance to interact with.
            webpage_url (str): The webpage URL.
        """        
        browser_instance.open_available_browser(url=webpage_url, headless=False, maximized=True)


class WebNavigationUtils:
    @staticmethod
    def get_webelement(browser_instance: Selenium, webelement_locator: str, parent_webelement: Optional[WebElement] = None) -> Optional[WebElement]:
        try:
            browser_instance.find_element(webelement_locator, parent=parent_webelement,)
        except ElementNotFound:
            return
        except Exception:
            raise

    @staticmethod
    def input_text(browser_instance: Selenium, webelement_locator: str, text_to_input: str) -> None:
        browser_instance.input_text_when_element_is_visible(locator=webelement_locator, text=text_to_input)

    @staticmethod
    def click_element(browser_instance: Selenium, webelement_locator: str) -> Optional[WebElement]:
        browser_instance.click_element_when_clickable(webelement_locator)

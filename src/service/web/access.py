from src.util.web import WebAccessUtils
from src import Selenium
from retry import retry


class WebAccess:
    def __init__(self) -> None:
        self._browser = WebAccessUtils.setup_browser()

    @retry(TimeoutError)
    def access_news_page(self) -> None:
        try:
            start_url = WebAccessUtils.get_web_locator('start')
            WebAccessUtils.access_webpage(browser_instance=self._browser, webpage_url=start_url)
        except TimeoutError:
            raise
        except Exception as error:
            print(f"Error when trying to access web page: [{type(error).__name__}] {error}")

    def run(self) -> Selenium:
        self.access_news_page()
        return self._browser

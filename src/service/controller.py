from src.service.web.access import WebAccess
from src.service.web.navigation import WebNavigation


class AutomationController:
    def __init__(self) -> None:
        pass

    def __run_web_automation(self) -> None:
        self._browser = WebAccess().run()
        WebNavigation(self._browser).run()

    def run(self) -> None:
        self.__run_web_automation()

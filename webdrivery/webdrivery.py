import structlog

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from webdrivery.settings import Settings
from webdrivery.singleton import Singleton


class WebDrivery(metaclass=Singleton):

    def init_browser(self, settings: Settings):
        self.d = None
        self.s = settings
        self.log = structlog.get_logger(self.__class__.__name__)
        self.log.debug('init_browser', settings=self.s.__dict__)

        d = self._get_web_driver(self.s.browser_name)
        d.set_window_position(self.s.window_position_x, self.s.window_position_y)
        d.set_window_size(self.s.window_width, self.s.window_height)
        d.implicitly_wait(self.s.implicit_wait)
        self.d = EventFiringWebDriver(d, self.s.event_listener) if self.s.event_listener else d

    def _get_web_driver(self, browser_name):
        select_driver_dict = {
            'chrome': self._init_chrome,
            'firefox': self._init_firefox,
            'safari': self._init_safari,
            'remote': self._init_remote
        }
        if browser_name not in select_driver_dict:
            raise ValueError(f'{browser_name}" browser does not supported')
        return select_driver_dict[browser_name]()

    def _init_firefox(self):
        o = webdriver.FirefoxOptions()
        if self.s.headless:
            o.add_argument('--headless')
        return webdriver.Firefox(options=o)

    def _init_safari(self):
        return webdriver.Safari()

    def _init_chrome(self):
        o = webdriver.ChromeOptions()
        o.add_argument('--disable-gpu')
        o.add_argument('--disable-dev-shm-usage')
        o.add_argument('--no-sandbox')
        o.add_argument('--disable-infobars')
        if self.s.headless:
            o.add_argument('--headless')
        if self.s.incognito:
            o.add_argument('--incognito')
        if self.s.mobile_device_name:
            o.add_experimental_option('mobileEmulation', {'deviceName': self.s.mobile_device_name})
        if self.s.user_agent:
            o.add_argument(f'user-agent={self.s.user_agent}')
        return webdriver.Chrome(options=o)

    def _init_remote(self):
        return webdriver.Remote(
            command_executor=self.s.command_executor,
            desired_capabilities=self.s.capabilities,
        )

    def get_driver(self) -> WebDriver:
        if self.d:
            return self.d
        raise ReferenceError('Please initialize browser: WebDrivery().init_browser(settings)')

    def s(self) -> Settings:
        if self.s:
            return self.s
        raise ReferenceError('Please initialize browser: WebDrivery().init_browser(settings)')

    def quit_browser(self):
        self.log.debug('quit_browser')
        if self.d:
            self.d.quit()
            self.d = None

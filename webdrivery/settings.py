from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class Settings:
    def __init__(
            self,
            host: str,
            browser_name: str = 'chrome',
            headless: bool = True,
            incognito: bool = True,
            implicit_wait: int = 4,
            timeout_wait: int = 4,
            highlight_style: str = 'outline: 2px dashed red',
            highlight_timeout: float = 0.4,
            type_slow_pause: float = 0.3,
            window_width: int = 1440,
            window_height: int = 900,
            window_position_x: int = 0,
            window_position_y: int = 0,
            mobile_device_name: str = '',
            user_agent: str = '',
            command_executor: str = '',
            capabilities: dict = None,
            event_listener: AbstractEventListener = None,
    ):
        if not host:
            raise AttributeError('host is not specified in Settings()')

        self.host = host
        self.browser_name = browser_name
        self.headless = headless
        self.incognito = incognito
        self.implicit_wait = implicit_wait
        self.timeout_wait = timeout_wait
        self.highlight_style = highlight_style
        self.highlight_timeout = highlight_timeout
        self.type_slow_pause = type_slow_pause
        self.window_width = window_width
        self.window_height = window_height
        self.window_position_x = window_position_x
        self.window_position_y = window_position_y
        self.mobile_device_name = mobile_device_name
        self.user_agent = user_agent
        self.command_executor = command_executor
        self.capabilities = capabilities
        self.event_listener = event_listener

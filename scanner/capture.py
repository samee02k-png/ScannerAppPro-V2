import win32gui


class TradeZeroCapture:

    def __init__(self):
        self.hwnd = None
        self.window_title = None

    def find_tradezero(self):
        """
        Finds the first visible window containing 'TradeZero'
        """

        self.hwnd = None
        self.window_title = None

        def enum_handler(hwnd, _):

            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd)

            if "tradezero" in title.lower():
                self.hwnd = hwnd
                self.window_title = title

        win32gui.EnumWindows(enum_handler, None)

        return self.hwnd is not None

    def get_window_rect(self):

        if self.hwnd is None:
            return None

        return win32gui.GetWindowRect(self.hwnd)

    def is_valid(self):

        if self.hwnd is None:
            return False

        return win32gui.IsWindow(self.hwnd)

    def get_title(self):

        return self.window_title
from frames.config import DisplayMode, config

class Response:
    message = ""
    error = False
    display = False

    def __init__(self, message, error = False, display = False):
        self.message = message
        self.error = error
        self.display = display

        if (config.display_mode == DisplayMode.ALWAYS):
            self.display = True
        elif (config.display_mode == DisplayMode.NEVER):
            self.display = False
        elif (config.display_mode == DisplayMode.SHOW_ERRORS and error):
            self.display = True


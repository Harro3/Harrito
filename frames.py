from enum import Enum

class DisplayMode(Enum):
    DEFAULT = 0,
    ALWAYS = 1,
    NEVER = 2,
    SHOW_ERRORS = 3


class Config:
    display_mode = DisplayMode.DEFAULT

    def dump(self):
        res = "```\n"
        
        res += "display mode: " + self.display_mode.name
        
        res += "\n```"

        return res

config = Config()

class Response:
    global config

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


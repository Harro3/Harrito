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


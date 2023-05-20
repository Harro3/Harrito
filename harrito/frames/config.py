from enum import Enum

class DisplayMode(Enum):
    DEFAULT = 0,
    ALWAYS = 1,
    NEVER = 2,
    SHOW_ERRORS = 3


class Config:
    display_mode = DisplayMode.DEFAULT
    text_color = (255, 255, 255)

    def dump(self):
        res = "```\n"
        
        res += "display mode: " + self.display_mode.name + "\n"
        res += "text color  : " + str(self.text_color) + "\n"
        
        res += "```"

        return res

config = Config()


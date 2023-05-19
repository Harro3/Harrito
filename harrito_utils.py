from sense_hat import SenseHat
from time import sleep
from enum import Enum
import requests
import subprocess

from endpoints import *

sense = SenseHat()

def sense_init():
    while True:
        try:
            requests.get("http://google.com", timeout=1)
            sense.clear((0,255,0))
            break
        except (requests.ConnectionError, requests.Timeout):
            sense.clear((255,0,0))
            sleep(0.5)
            sense.clear()
            sleep(0.5)
    sleep(1)
    sense.clear()


class Command:
        
    endpoint = None
    command = ""
    args = []
    message = None

    def __init__(self, message):
        self.message = message
        argv = message.content.split(" ")
        self.args = argv[1:]

        self.command = argv[0].lower()

        if (self.command in endpointsDict):
            self.endpoint = endpointsDict[self.command]    

    async def resolve(self):
        if (self.endpoint == None):
            return Response("Command not found: " + self.command, True)

        return self.endpoint(self)



async def process_msg(message):
    comm = Command(message)
    sense.clear()
    response = await comm.resolve()
    col = (255, 255, 255)
    if (response.error):
        response.message = "ERROR: " + response.message
        col = (255, 0, 0)

    await comm.message.channel.send(response.message)
    if (response.display):
        sense.show_message(response.message, text_colour=col, scroll_speed=0.05)



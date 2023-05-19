from sense_hat import SenseHat
import requests
from time import sleep

sense = SenseHat()

def hardware_init():
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

def display_message(message, col = (255,255,255)):
    sense.show_message(message, text_colour=col, scroll_speed=0.05)

def get_temperature():
    return sense.get_temperature()

def get_humidity():
    return sense.get_humidity()

def get_pressure():
    return sense.get_pressure()
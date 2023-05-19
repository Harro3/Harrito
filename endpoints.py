import subprocess
from sense_hat import SenseHat
from enum import Enum
from frames import Response, DisplayMode, config

sense = SenseHat()

def echo(command):
    if (len(command.args) == 0):
        return Response("echo: no args provided", True)
    response = ""
    for arg in command.args:
        response += arg + " "
    return Response(response, display=True)


def get(command):
    if (len(command.args) == 0):
        return Response("get: no args provided", True)

    res = command.args[0]
    if (res == "temperature"):
        return Response(str(int(sense.get_temperature())) + " degrees")
    elif (res == "humidity"):
        return Response(str(int(sense.get_humidity())) + "%")
    elif (res == "pressure"):
        return Response(str(int(sense.get_pressure())) + " milibars")
    
    elif (res == "ip"):
        ip = str(subprocess.check_output(("hostname", "-I")))
        ip = ip.replace("b", "")
        ip = ip.replace("\\n", "")
        ip = ip.replace("'", "")
        return Response(ip)
    
    elif (res == "config"):
        return Response(config.dump())

    else:
        return Response("get: ressource not found: " + res, True)



def configure(command):
    if (len(command.args) != 2):
        return Response("configure: there must be two arguments", True)
    
    option = command.args[0].lower()
    value = command.args[1].lower()

    if (option == "display_mode"):
        if (value == "always"):
            config.display_mode = DisplayMode.ALWAYS
        elif (value == "never"):
            config.display_mode = DisplayMode.NEVER
        elif (value == "default"):
            config.display_mode = DisplayMode.DEFAULT
        elif (value == "show_errors"):
            config.display_mode = DisplayMode.SHOW_ERRORS
        else:
            return Response("configure display_mode: unrecognized value \""+value+"\"", True)
    
    else:
        return Response("configure: unrecognized option \""+option+"\"", True)
    
    return Response("config updated")


endpointsDict = {
    "echo" : echo,
    "get"  : get,
    "configure" : configure
}

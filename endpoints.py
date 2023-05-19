import subprocess
from sense_hat import SenseHat

sense = SenseHat()

class Response:
    message = ""
    error = False
    display = True

    def __init__(self, message, error = False, display = True):
        self.message = message
        self.error = error
        self.display = display


def echo(command):
    if (len(command.args) == 0):
        return Response("echo: no args provided", True)
    response = ""
    for arg in command.args:
        response += arg + " "
    return Response(response)


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

    else:
        return Response("get: ressource not found: " + res, True)







endpointsDict = {
    "echo" : echo,
    "get"  : get
}

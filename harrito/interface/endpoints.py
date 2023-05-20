import subprocess

from frames.config import DisplayMode, config
from frames.response import Response
import interface.hardware as hardware

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
        return Response(str(int(hardware.get_temperature())) + " degrees")
    elif (res == "humidity"):
        return Response(str(int(hardware.get_humidity())) + "%")
    elif (res == "pressure"):
        return Response(str(int(hardware.get_pressure())) + " milibars")
    
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
    if (len(command.args) < 2):
        return Response("configure: there must be at least two arguments", True)
    
    option = command.args[0].lower()

    if (option == "display_mode"):
        value = command.args[1].lower()
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
    elif (option == "text_color"):
        try:
            r = int(command.args[1])
            g = int(command.args[2])
            b = int(command.args[3])
            config.text_color = (r,g,b)
        except:
            return Response("configure text_color: invalid arguments", False)

    else:
        return Response("configure: unrecognized option \""+option+"\"", True)
    
    return Response("config updated")

def help(command):
    return Response(f"Hi, I am a general purposes bot running on Harro's raspberry!\nHere is a fancy doc: https://harro3.github.io/Harrito/, \nCommands must begin with \"!\" in servers")

def alert(command):
    hardware.alert()
    return Response("Alert given")

def shell(command):
    if (command.message.author.id != 421810982998900738):
        return Response("You are not allowed to run this command (cheh)")
    result = subprocess.run(command.args, stdout=subprocess.PIPE)
    return Response("```\n" + result.stdout.decode('utf-8') + "```")

endpointsDict = {
    "echo" : echo,
    "get"  : get,
    "configure" : configure,
    "help":help,
    "alert" : alert,
    "shell" : shell
}

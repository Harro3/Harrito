from interface.endpoints import endpointsDict
from frames.response import Response

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

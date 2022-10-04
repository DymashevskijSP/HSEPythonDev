import json
from concurrent.futures import ThreadPoolExecutor

import grpc

from HSEPythonDev.src.protos.HelloWorld_pb2 import Response
from HSEPythonDev.src.protos.HelloWorld_pb2_grpc import (HelloWorldControllerServicer,
                                                         add_HelloWorldControllerServicer_to_server)


class Service(HelloWorldControllerServicer):

    def Create(self, request, context) -> Response:
        """
        returns: Response: status is process status and json contains message: request.text, request.name
        """
        name = request.name
        message = request.text
        return Response(status=200, json=json.dumps({'message': message + (', ' + name if name else '!')}))

    def Retrieve(self, request, context) -> Response:
        """
        returns: Response: status is process status and json contains message: Hello, request.name
        """
        name = request.name
        return Response(status=200, json=json.dumps({'message': 'Hello, ' + name + '!'}))

def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_HelloWorldControllerServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
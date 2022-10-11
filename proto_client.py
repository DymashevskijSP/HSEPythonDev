import grpc

from HSEPythonDev.src.protos.HelloWorld_pb2 import GetRequest, PostRequest
from HSEPythonDev.src.protos.HelloWorld_pb2_grpc import HelloWorldControllerStub


def main():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = HelloWorldControllerStub(channel)

        print(client.Retrieve(GetRequest(name='Alesha')).json)
        creation = client.Create(
            PostRequest(name="Sergey", text='You are the best'))

        print(creation.json)


if __name__ == "__main__":
    main()

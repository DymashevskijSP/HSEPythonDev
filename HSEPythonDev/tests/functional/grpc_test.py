import json
import grpc
from unittest import TestCase
from HSEPythonDev.src.protos.HelloWorld_pb2 import Response, GetRequest, PostRequest
from HSEPythonDev.src.protos.HelloWorld_pb2_grpc import (HelloWorldControllerStub,
                                                         add_HelloWorldControllerServicer_to_server)
from concurrent import futures
from proto_server import Service


class TestHelloWorld(TestCase):
    port = 50051
    server_class = Service

    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        add_HelloWorldControllerServicer_to_server(self.server_class(), self.server)
        self.server.add_insecure_port(f'[::]:{self.port}')
        self.server.start()

    def tearDown(self):
        self.server.stop(None)

    def test_server(self):
        with grpc.insecure_channel(f'localhost:{self.port}') as channel:
            stub = HelloWorldControllerStub(channel)
            response = stub.Retrieve(GetRequest(name='Jack'))
        self.assertEqual(response.json, '{"message": "Hello, Jack!"}')
        self.assertEqual(response.status, 200)

    def test_post(self):
        text = 'You are the best'
        with grpc.insecure_channel(f'localhost:{self.port}') as channel:
            stub = HelloWorldControllerStub(channel)
            response = stub.Create(PostRequest(text=text, name='Alesha'))
        self.assertEqual(response.json, '{"message": "You are the best, Alesha"}')
        self.assertEqual(response.status, 200)

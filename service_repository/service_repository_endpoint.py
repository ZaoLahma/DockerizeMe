from flask import Flask
from flask_restful import Resource, Api
from service_discovery.service_discovery_request import ServiceDiscoveryRequest

flask_inst = Flask(__name__)
flask_rest_inst = Api(flask_inst)

class ServiceRepositoryEndpoint:
    def __init__(self):
        self.flask_inst = flask_inst
        self.flask_rest_inst = flask_rest_inst

    def host(self, host, port, debug):
        self.flask_inst.run(host, port, debug)

    @staticmethod
    @flask_inst.route("/")
    def hello():
        return "Hello world from flask!"
    
    def add_resource(self, api, path):
        self.flask_rest_inst.add_resource(api, path)
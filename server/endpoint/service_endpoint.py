from flask import Flask
from flask_restful import Resource, Api
from services.service_discovery.service_discovery_request import ServiceDiscoveryRequest

flask_inst = Flask(__name__)
flask_rest_inst = Api(flask_inst)

class ServiceEndpoint:
    def __init__(self, name, app_rel_path):
        self.flask_inst = flask_inst
        self.flask_inst.template_folder = app_rel_path + "/templates"
        self.flask_rest_inst = flask_rest_inst

    def host(self, host, port, debug, reload):
        print("ServiceEndpoint - hosting on <{}>".format((host, port)))
        self.flask_inst.run(host, port, debug=debug, use_reloader=reload)

    @staticmethod
    @flask_inst.route("/")
    def hello():
        return "<html><head><title>Install ok</title></head><body>If you see this, the application is up and running</body></html>"
    
    def add_resource(self, api, *paths):
        self.flask_rest_inst.add_resource(api, *paths)
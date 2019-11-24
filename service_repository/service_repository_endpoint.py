from flask import Flask

flask_inst = Flask(__name__)

class ServiceRepositoryEndpoint:
    def __init__(self):
        self.flask_inst = flask_inst

    def host(self, host, port, debug):
        self.flask_inst.run(host, port, debug)

    @staticmethod
    @flask_inst.route("/")
    def hello():
        return "Hello world from flask!"
from flask_restful import Resource
from .service_repository import ServiceRepository
from flask_restful.reqparse import RequestParser

class ServicesAPI(Resource):
    def __init__(self):
        self.service_repository = ServiceRepository()

    def get(self):
        print("Get")
        services = []
        for key in self.service_repository.get_all_services():
            print(key)
            services.append(self.service_repository.get_all_services()[key])
        return {'result' : 'success', 'data' : services}, 200

    def post(self):
        parser = RequestParser()

        parser.add_argument("identifier", required=True)
        parser.add_argument("name", required=True)
        parser.add_argument("version", required=True)
        parser.add_argument("address", required=True)
        parser.add_argument("port", required=True)
        parser.add_argument("path", required=True)

        args = parser.parse_args()

        self.service_repository.add_service(args["identifier"], args)

        return {'result' : 'success'}, 201
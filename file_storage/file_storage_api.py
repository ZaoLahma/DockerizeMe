from services.service_repository.client.services_client_api import ServicesClientAPI
from services.service_discovery.service_discovery_context import ServiceDiscoveryCtxt
from .file_storage_context import FileStorageCtxt
from nw_misc.nw_misc import NwMisc
from flask_restful import Resource

class FileStorageAPI(Resource):
    @staticmethod
    def publish():
        print("File storage publishing its service...")
        ServicesClientAPI.register_service("file-storage", "File storage", 1, NwMisc.get_own_address(), 8081, "filestorage")
        print("File storage ready to store files to {}".format(FileStorageCtxt.storage_path))

    def get(self):
        return '{result : success}', 200

    def put(self, file_name):
        print("put called with file_name: {}".format(file_name))
        return '{result : success}', 200
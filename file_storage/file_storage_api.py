from service_repository.client.services_client_api import ServicesClientAPI
from service_discovery.service_discovery_context import ServiceDiscoveryCtxt
from .file_storage_context import FileStorageCtxt
from flask_restful import Resource

class FileStorageAPI(Resource):
    def __init__(self):
        print("File storage initializing...")
<<<<<<< HEAD
        ServicesClientAPI.register_service(ServiceDiscoveryCtxt.multicast_address, "file-storage", "File storage", 1, "127.0.0.1", 8083)
=======
        ServicesClientAPI.register_service("file-storage", "File storage", 1, "127.0.0.1", 8083, "filestorage")
>>>>>>> File storage started
        print("File storage ready to store files to {}".format(FileStorageCtxt.storage_path))

    def put(self, file_name):
        return '{result : success}', 200
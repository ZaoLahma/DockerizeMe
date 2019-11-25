from services.service_repository.client.services_client_api import ServicesClientAPI
from services.service_discovery.service_discovery_context import ServiceDiscoveryCtxt
from .file_storage_context import FileStorageCtxt
from nw_misc.nw_misc import NwMisc
from flask_restful import Resource
from flask import request
from flask import send_file
from io import BytesIO
from magic import Magic
from flask import render_template
from flask import make_response

class FileStorageAPI(Resource):
    @staticmethod
    def publish():
        print("File storage publishing its service...")
        ServicesClientAPI.register_service("file-storage", "File storage", 1, NwMisc.get_own_address(), 8081, "filestorage")
        print("File storage ready to store files to {}".format(FileStorageCtxt.storage_path))

    def get(self, resource):

        if ("list.html" == resource):
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('base.html'), 200, headers)
        else:
            with open(FileStorageCtxt.storage_path + resource, 'rb') as bites:
                mime = Magic(mime=True)
                return send_file(BytesIO(bites.read()), attachment_filename=resource, mimetype=mime.from_file(FileStorageCtxt.storage_path + resource))
    
    def put(self, file_name):

        with open(FileStorageCtxt.storage_path + file_name, "wb+") as new_file:
            new_file.write(request.get_data())

        return {'result' : 'success', 'file-name' : file_name}, 201
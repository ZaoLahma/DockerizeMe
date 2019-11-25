from endpoint.service_endpoint import ServiceEndpoint
from services.service_discovery.service_discovery_context import ServiceDiscoveryCtxt
from file_storage.file_storage_context import FileStorageCtxt
from file_storage.file_storage_api import FileStorageAPI
from nw_misc.nw_misc import NwMisc

if __name__ == "__main__":
    print("File storage main called")
    service_discovery_port = 4070
    file_storage_port = 8081
    multicast_address = ("224.3.29.71", service_discovery_port)
    ServiceDiscoveryCtxt.multicast_address = multicast_address
    FileStorageCtxt.storage_path = '/app/file_storage/files'

    FileStorageAPI.publish()

    service_endpoint = ServiceEndpoint()
    service_endpoint.add_resource(FileStorageAPI, '/filestorage/<string:file_name>')
    service_endpoint.host(NwMisc.get_own_address(), file_storage_port, True, True)
    
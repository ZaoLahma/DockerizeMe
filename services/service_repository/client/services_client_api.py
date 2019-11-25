import requests
from services.service_discovery.service_discovery_request import ServiceDiscoveryRequest

from services.service_discovery.service_discovery_context import ServiceDiscoveryCtxt

class ServicesClientAPI:
    @staticmethod
    def register_service(identifier, name, version, address, port, path):
        print("Attempting to retrieve service storage from {}".format(ServiceDiscoveryCtxt.multicast_address))
        services_address = ServiceDiscoveryRequest.getServiceRepository(ServiceDiscoveryCtxt.multicast_address)
        print("Services address: {}".format(services_address))
        services_endpoint = "http://{}:{}/{}".format(services_address[0], services_address[1], services_address[2])

        print("Registering service {} at {}".format(name, services_endpoint))

        data = {'identifier' : identifier, 
                'name' : name, 
                'version' : version, 
                'address' : address,
                'port' : port,
                'path' : path} 
  
        response = requests.post(url = services_endpoint, data = data)

        print("Received response: {}".format(response))
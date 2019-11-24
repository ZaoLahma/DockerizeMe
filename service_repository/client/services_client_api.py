import requests
from service_discovery.service_discovery_request import ServiceDiscoveryRequest

class ServicesClientAPI:
    @staticmethod
    def register_service(multicast_address, identifier, name, version, address, port):
        print("Attempting to retrieve service storage from {}".format(multicast_address))
        services_address = ServiceDiscoveryRequest.getServiceRepository(multicast_address)
        print("Services address: {}".format(services_address))
        services_endpoint = "http://{}:{}/services".format(services_address[0], services_address[1])

        print("Registering service {} at {}".format(name, services_endpoint))

        data = {'identifier' : identifier, 
                'name' : name, 
                'version' : version, 
                'address' : address,
                'port' : port} 
  
        response = requests.post(url = services_endpoint, data = data)

        print("Received response: {}".format(response))
from endpoint.service_endpoint import ServiceEndpoint
from services.service_repository.service_api import ServicesAPI
from services.service_discovery.service_discovery_endpoint import ServiceDiscoveryEndpoint
from services.service_discovery.service_discovery_context import ServiceDiscoveryCtxt
import threading

if __name__ == "__main__":
    print("Services main called")
    service_discovery_port = 4070
    services_port = 8080
    multicast_address = ("224.3.29.71", service_discovery_port)
    ServiceDiscoveryCtxt.multicast_address = multicast_address

    service_discovery = ServiceDiscoveryEndpoint(services_port)
    service_discovery_thread = threading.Thread(target=service_discovery.run)
    service_discovery_thread.start()

    service_endpoint = ServiceEndpoint()
    service_endpoint.add_resource(ServicesAPI, '/services')
    service_endpoint.host('0.0.0.0', services_port, True, True)

    service_discovery_thread.active = False
    
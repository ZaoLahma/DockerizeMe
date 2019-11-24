from service_repository.service_repository_endpoint import ServiceRepositoryEndpoint
from service_repository.services_api import ServicesAPI

if __name__ == "__main__":
    endpoint = ServiceRepositoryEndpoint()
    endpoint.add_resource(ServicesAPI, '/services')
    endpoint.host('0.0.0.0', 8080, True)
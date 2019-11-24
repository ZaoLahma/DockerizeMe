from service_repository.service_repository_endpoint import ServiceRepositoryEndpoint

if __name__ == "__main__":
    endpoint = ServiceRepositoryEndpoint()
    endpoint.host('0.0.0.0', 8080, True)
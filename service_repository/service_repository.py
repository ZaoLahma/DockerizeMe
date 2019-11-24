import json

class ServiceRepository:
    services_inst = {}
    def __init__(self):
        self.services = ServiceRepository.services_inst

    def get_all_services(self):
        print(self.services)
        print(self)
        return self.services

    def get_service(self, service_identifier):
        return self.services[service_identifier]

    def add_service(self, service_identifier, service):
        self.services[service_identifier] = service
        print(self.services)
        print(self)

    def remove_service(self, service_identifier):
        del self.services[service_identifier]
import socket
import json
import struct

class ServiceDiscoveryRequest():
    @staticmethod
    def getServiceRepository(multicast_address):
        service_discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ttl = struct.pack('b', 1)
        service_discovery_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        request = '{"request" : "service-repository-address"}'

        retVal = None

        try:
            sent = service_discovery_socket.sendto(request.encode(), multicast_address)
            print("Sent {}".format(sent))
            response = service_discovery_socket.recv(4096)
            print("Response: {}".format(response.decode()))
            response = json.loads(response.decode())
            address = response["response"]["address"]
            port_no = response["response"]["port-no"]
            path = response["response"]["path"]
            retVal = (address, port_no, path)
        finally:
            service_discovery_socket.close()

        return retVal
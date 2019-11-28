import socket
import struct
import json
from .service_discovery_context import ServiceDiscoveryCtxt
from nw_misc.nw_misc import NwMisc

class ServiceDiscoveryEndpoint:
    def __init__(self, service_repository_port_no):
        self.service_repository_port_no = service_repository_port_no

        multicast_server_address = ("", ServiceDiscoveryCtxt.multicast_address[1])

        print("multicast_server_address {}".format(multicast_server_address))

        group = socket.inet_aton(ServiceDiscoveryCtxt.multicast_address[0])
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)

        self.multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        self.multicast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.multicast_socket.bind(multicast_server_address)
        self.multicast_socket.settimeout(1)

        self.address = None
        self.active = False

        print("__init__ done")

    def run(self):
        print("Starting service discovery endpoint at {}".format(ServiceDiscoveryCtxt.multicast_address))
        self.active = True
        while True == self.active:
            try:
                data = self.multicast_socket.recvfrom(4096)
            except socket.timeout:
                pass
            except:
                raise
            else:
                print("Data: {}".format(data))
                request = json.loads(data[0].decode())
                client_request = request["request"]
                if "service-repository-address" == client_request:
                    print("ServiceDiscoveryListener - Returning {} on port_no: {}".format(NwMisc.get_own_address(), self.service_repository_port_no))

                    response = {}
                    response["response"] = {}
                    response["response"]["port-no"] = self.service_repository_port_no
                    response["response"]["address"] = NwMisc.get_own_address()
                    response["response"]["path"] = "services"

                    response = json.dumps(response)

                    client_endpoint = data[1]
                    response_socket = None
                    try:
                        response_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        response_socket.sendto(response.encode(), client_endpoint)
                    finally:
                        response_socket.close()
                else:
                    print("Ignoring request for {}".format(client_request))
        self.multicast_socket.close()
        print("Stopped service discovery endpoint at {}".format(ServiceDiscoveryCtxt.multicast_address))

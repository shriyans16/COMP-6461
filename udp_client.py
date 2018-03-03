import argparse
import ipaddress
import socket
import _thread

from packet import Packet

def runClient(routerAddress, routerPort, serverAddress, serverPort):
    ip_peer = ipaddress.ip_address(socket.gethostbyname(serverAddress))
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = 10
    try:
        message = "Message to server"
        message = message + "\r\n"
        packet = Packet(packet_type=0,
                        seq_num=1,
                        peer_ip_addr=ip_peer,
                        peer_port=serverPort,
                        is_last_packet=True,
                        payload=message.encode("utf-8"))
        connection.sendto(packet.convertToBytes(), (routerAddress, routerPort))
        print('Sending "{}" to router'.format(message))

        connection.settimeout(timeout)
        print('Waiting for a response')
        response, sender = connection.recvfrom(1024)
        packet = Packet.from_bytes(response)

        print('Response from the server !')
        print('Router: ', sender)
        print('Packet: ', packet)
        print('Message from server: ' + packet.payload.decode("utf-8"))

    except socket.timeout:
        print('No response after {}s'.format(timeout))
    finally:
        connection.close()


parser = argparse.ArgumentParser()
parser.add_argument("--rhost", help="router host", default="localhost")
parser.add_argument("--rport", help="router port", type=int, default=3000)

parser.add_argument("--shost", help="server host", default="localhost")
parser.add_argument("--sport", help="server port", type=int, default=8007)
args = parser.parse_args()

#run_client(args.routerhost, args.routerport, args.serverhost, args.serverport)

# Creating threads.
try:
    _thread.start_new_thread(runClient, (args.rhost, args.rport, args.shost, args.sport))
    _thread.start_new_thread(runClient, (args.rhost, args.rport, args.shost, args.sport))
    _thread.start_new_thread(runClient, (args.rhost, args.rport, args.shost, args.sport))
except:
    print("Thread not working.")

while 1:
    pass

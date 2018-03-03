import argparse
import socket

from packet import Packet


def run_server(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        connection.bind(('', port))
        print('Port : ', port)
        while True:
            data, sender = connection.recvfrom(1024)
            handlingClient(connection, data, sender)

    finally:
        connection.close()


def handlingClient(conn, data, router):
    try:
        packet = Packet.from_bytes(data)
        print('Client Sending.')
        print("Router: ", router)
        print("Packet: ", packet)
        print("Client Message: ", packet.payload.decode("utf-8"))

        packet.payload = "Hello Client !".encode("utf-8")
        conn.sendto(packet.convertToBytes(), router)

    except Exception as e:
        print(e)


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="echo server port", type=int, default=8007)
args = parser.parse_args()
run_server(args.port)
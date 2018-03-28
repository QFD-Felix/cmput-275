import sys
from cs_message import *
from server import *


vertex_coord = {}
vertex_coord = read_vertex_coord("edmonton-roads-2.0.1.txt")
g = read_city_graph("edmonton-roads-2.0.1.txt")
"""
A very basic test server that can exercise the route finding client,
as well as display the diagnostic messages that it generates.

You can use this to test your client's basic functionality, and to
see if a large path that consumes too much memory will be properly
handled.

Typically run with
    python3 dummy_server.py -s /dev/ttyACM0

optional arguments:
  -h, --help            show this help message and exit
  -d0                   Debug off
  -s [SERIAL_PORT_NAME]
                        Set serial port for protocol

"""


def protocol(serial_in, serial_out):
    # simple echo protocol
    while True:
        while True:
            msg = receive_msg_from_client(serial_in)
            log_msg(msg)
            msg = msg.strip()
            if msg[0] == "R":
                break

        # Hope that it's a properly formatted R message
        coords = msg[2:].split()

        if len(coords) != 4:
            continue

        (lat_s, lon_s, lat_e, lon_e) = coords
        lat_s = int(lat_s)
        lon_s = int(lon_s)
        lat_e = int(lat_e)
        lon_e = int(lon_e)
        delta_lat = lat_e - lat_s
        delta_lon = lon_e - lon_s

        # write a fake waypoint path to client, make n large to break the
        # client.
        start = check_cloest_point(lat_s, lon_s)
        end = check_cloest_point(lat_e, lon_e)
        path = least_cost_path(g, start, end, cost_distance)
        n = len(path)
        print("Path length: {}".format(n))
        send_msg_to_client(serial_out, "N {}" .format(n))
        while True:
            msg = receive_msg_from_client(serial_in)
            if msg[0] == 'A':
                break
        print(len(path))
        for v in path:
            print("W {} {}" .format(vertex_coord[v][0],vertex_coord[v][1]))
            send_msg_to_client(serial_out, "W {} {}" .format(vertex_coord[v][0],vertex_coord[v][1]))
            msg = receive_msg_from_client(serial_in)
            log_msg(msg)
        if msg[0] == 'A':
            send_msg_to_client(serial_out, "E")


def main():

    import argparse
    parser = argparse.ArgumentParser(
        description='Client-server message test.',
        formatter_class=argparse.RawTextHelpFormatter,
        )

    parser.add_argument("-d0",
        help="Debug off",
        action="store_false",
        dest="debug")

    parser.add_argument("-s",
        help="Set serial port for protocol",
        nargs="?",
        type=str,
        dest="serial_port_name",
        default="/dev/ttyACM0")

    args = parser.parse_args()

    debug = args.debug

    set_logging(debug)

    # this imports serial, and provides a useful wrapper around it
    import textserial

    serial_port_name = args.serial_port_name;
    log_msg("Opening serial port: {}".format(serial_port_name))

    # Open up the connection
    baudrate = 9600  # [bit/seconds] 115200 also works

    # Run the server protocol forever

    # The with statment ensures that if things go bad, then ser
    # will still be closed properly.
    # errors='ignore' allows any 1 byte character, not just the usual
    # ascii range [0,127]

    with textserial.TextSerial(
        serial_port_name, baudrate, errors='ignore', newline=None) as ser:
        protocol(ser, ser)

if __name__ == "__main__":
    main()

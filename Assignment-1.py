#Author :	1) Maniar Meet (40039203)
#			2) Athalye Shriyans (40037637)
import argparse
from httpclient_library import writeToFile, redirect, http_post, http_get


parser = argparse.ArgumentParser(description="Description for custom HTTP Client")
parser.add_argument("gp", choices=['get', 'post'])
parser.add_argument('--verbose', action='store_true', help='verbose flag')
parser.add_argument('-o')
parser.add_argument('--h', '-H', action='append', help='k:v, may repeat')
parser.add_argument('--data', metavar='inline-data')
parser.add_argument('-f', '--file')
parser.add_argument('url')
args = parser.parse_args()
http_get(args)
import sys
import json
import yaml
from rest import Rest
from streamreader import StreamReader

CONFIG = yaml.load(file('config.yaml', 'rb'))

def computeVBRange(vbuckets):
    start = 0
    end = vbuckets

    if len(sys.argv) == 3:
        total = int(sys.argv[2])
        vbs_per_spout = vbuckets/total
        start = int(sys.argv[1])*vbs_per_spout
        end = start + vbs_per_spout

    return start, end

class DCPStream():

    def __init__(self):
        cbconf = CONFIG['couchbase']
        ip = cbconf['ip']
        port = int(cbconf['port'])
        username = cbconf['username']
        password = cbconf['password']
        vbuckets = cbconf['vbuckets']
        rest = Rest(ip, port, username, password)
        start, end = computeVBRange(vbuckets)
        self.reader = StreamReader(rest, start, end)

    def nextTuple(self):

        try:
            vb, msg = self.reader.response().next()
            if msg and msg['opcode'] == 87:
                print msg['value']
        except StopIteration:
            print "error"

stream = DCPStream()
while True:
    stream.nextTuple()

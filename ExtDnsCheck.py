import sys
import json
import dns
import argparse
from dns import resolver


class ResolutionTarget(object):

    def __init__(self, name, rtype):
        self.name = name
        self.rtype = rtype

    def forwardresolutionrequest(self):
        externalDNS = dns.resolver.Resolver()
        if overrideDNSIP == True:
            externalDNS.nameservers = [overrideDNSIPAddr]
        else:
            externalDNS.nameservers = ['8.8.8.8', '8.8.4.4']

        try:
            returndata = externalDNS.query(self.name, self.rtype)
            for rdata in returndata:
                print(self.name, "Was found at", rdata, "and Record type:", self.rtype)
        except:
            print(self.name, ": Query failed resolution on:",
                  externalDNS.nameservers[0])
            pass


dataErrorTypes = (IOError, ValueError)
parser = argparse.ArgumentParser(description='Parse positional'
                                             'arguments to script')
parser.add_argument("--json", help="/path/to/json/file")
parser.add_argument(
    "--override_dns", help="You must also provide --dnsaddr", action="store_true")
parser.add_argument("--dnsaddr", help="Enter a DNS or DNS seperated by a comma (8.8.8.8, 4.4.4.4)"
                                      " Requires --override_dns")
args = parser.parse_args()
jsonHostFile = args.json
overrideDNSIP = args.override_dns

if args.override_dns == True:
    overrideDNSIPAddr = args.dnsaddr
else:
    overrideDNSIP = False


try:
    with open(jsonHostFile) as f:
        jsonHostDict = json.load(f)
except dataErrorTypes:
    print("The supplied argument to this application"
          " causes an exception on I/O, is the file accessible/readable?")

absMin = 0
absIndexValue = {}
metaType = ["machines", "databases", "loadbalancers"]
for metaTypeVal in metaType:
    currentMeta = metaTypeVal
    valueMax = len(jsonHostDict[currentMeta])
    absIndexValue.update({currentMeta: valueMax})
    absIndexValueMax = absIndexValue[currentMeta]
    try:
        for hostCount in range(absMin, absIndexValueMax):
            hostStatus = ResolutionTarget(jsonHostDict[currentMeta][hostCount]['id'],
                                          jsonHostDict[currentMeta][hostCount]['RecordType'])
            hostStatus.forwardresolutionrequest()
    except dataErrorTypes:
        print(hostStatus)
        pass

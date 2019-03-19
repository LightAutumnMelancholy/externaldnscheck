Basic usage:  python3 ExtDnsCheck.py --json </path/to/json/formatted/assetsfile.json> || --json <pathtofile> --override_dns --dns_addr <?.?.?.?>
Requires: dnspython (dns)

Testing internal vs external resolution: Modify the DNS entry in externalDNS.nameservers in the ResolutionTarget class.
This could be used in production to check, you can easily hardcode if you require. Host files with JSON shouldn't change often, and we can expand with additional elements later.

Exmaple JSON syntax:

{
            "machines": [
                {
                    "id": "rdudc1.gopda.com",
                    "RecordType": "A"
                },
                { 
                    "id": "rdudc2.gopda.com",
                    "RecordType": "A"
                }
            ],
            "databases": [
                {
                    "id": "dbwhatever.gopda.com",
                    "RecordType": "A"
                },
                {
                    "id": "dbhost02",
                    "RecordType": "CNAME"
                } 
            ],
            "loadbalancers": [
                {
                    "id": "elb01",
                    "RecordType": "A"
                 },
                {
                    "id": "nlb01",
                    "RecordType": "A"
                 }
            ]
}


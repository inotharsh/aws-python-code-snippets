'''This snippet can create a list of s3 objects in more than one bucket with no limitation of number of objects'''
'''This works with a role based access'''

import boto3

s3_cli = boto3.client('s3')
s3_res = boto3.resource('s3')
bucket_list = ['']

for bucket in bucket_list:
    kwargs = {'Bucket': bucket}
    while True:
        response = s3_cli.list_objects_v2(**kwargs)
        #print(response)
        for item in response['Contents']:
            print(item['Key'])
        try:
            kwargs['ContinuationToken'] = response['NextContinuationToken']
        except KeyError:
            break
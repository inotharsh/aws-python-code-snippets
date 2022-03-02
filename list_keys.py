'''This snippet can create a list of s3 objects in more than one bucket with no limitation of number of objects'''


'''client'''

import boto3

s3_cli = boto3.client('s3')
#s3_cli = boto3.client('s3', aws_access_key_id = '', aws_secret_access_key = '')
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
            
'''resource'''

import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('mybucket')
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)

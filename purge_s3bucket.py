warning = '''WARNING
This code will completely wipe the bucket!!!
All the current and versioned files will be permanently removed/deleted'''

import boto3

print(warning)
read = input('Have you read the warning? (y/n): ').lower()

bucket = ''

if read == 'y':
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket.object_versions.delete()
else:
    print(f"Read {warning}")
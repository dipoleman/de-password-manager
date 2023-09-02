import boto3
from datetime import datetime
from pprint import pprint

#timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#bucket_name = f'task-one-bucket-{timestamp}'
# David's bucket
bucket_name = 'task-one-bucket-20230719110953'
# Michael's bucket
# bucket_name = 'task-one-bucket-20230719114840'
# print(bucket_name)


s3 = boto3.client('s3')
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint':'eu-west-2'
    }
)

s3.upload_file('text1.txt',bucket_name,'text1.txt')
s3.upload_file('text2.txt',bucket_name,'text2.txt')

contents = s3.list_objects_v2(Bucket=bucket_name)

file_names = [object['Key'] for object in contents['Contents']]
pprint(file_names)

response = s3.get_object(Bucket=bucket_name, Key='text1.txt')
content = response['Body'].read().decode('utf-8')
pprint(content)

deleted_objects = s3.delete_objects(
    Bucket=bucket_name,
    Delete={
        'Objects': [
            {
                'Key': 'text1.txt',
            },
            {
                'Key': 'text2.txt'
            }
        ],
    },
)

pprint(deleted_objects)

deleted_bucket = s3.delete_bucket(Bucket=bucket_name)
pprint(deleted_bucket)

list_bucket = s3.list_buckets()
bucket_names = [object['Name'] for object in list_bucket['Buckets']]
pprint(bucket_names)
import boto3
from botocore.exceptions import NoCredentialsError

import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id="AKIAQYEI4VZPM6GKEMXF",
    aws_secret_access_key="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",
    region_name="eu-north-1"
)

import boto3
from botocore.exceptions import ClientError

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_path.split('/')[-1]
    
    # Create S3 client (uses credentials from ~/.aws/credentials or env vars)    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to s3://{bucket_name}/{object_name}")
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False
    return True

from decouple import config
import os
os.environ['AWS_ACCESS_KEY_ID'] = config('AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY'] = config('AWS_SECRET_ACCESS_KEY')
os.environ['AWS_DEFAULT_REGION'] = config('AWS_DEFAULT_REGION')
# Replace these with your details
file_path = "C:/Users/23434813/Downloads/file1.pdf"  # Replace with your PDF file path
bucket_name = 'ehealthhubbucket'      # Your S3 bucket name
object_name = 'uploads/file.pdf'      # Optional: S3 path/key (defaults to file name)

upload_file_to_s3(file_path, bucket_name, object_name)

import boto3

ACCESS_KEY = 'ba88124bb9f211337bbc6c103330c249'
SECRET_KEY = '863ba92413967d939d8cd1296b9010d62099712bb76c44fde5ffcea771822180'
BUCKET_NAME = 'group25022025'
ENDPOINT = 'https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com'
# ---------------------------------------------------------------------------


PUBLIC_URL = 'https://pub-d2b580fe400441b19434564174b8efa7.r2.dev'

s3client = boto3.client(
    's3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='EEUR'
)


# UPLOAD FILE

target_file_name = 'images/66666666666666666.jpeg'
s3client.upload_file('spring.jpeg', BUCKET_NAME, target_file_name)
print(f'{PUBLIC_URL}/{target_file_name}')
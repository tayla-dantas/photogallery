import boto3,uuid

s3_client = boto3.client('s3',aws_access_key_id='AKIASZ6M73INSE3WJPM4',
         aws_secret_access_key= '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')
s3_resource = boto3.resource('s3',aws_access_key_id='AKIASZ6M73INSE3WJPM4',
         aws_secret_access_key='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')

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': 'es-east-1'})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

first_bucket_name, first_response = create_bucket(
      bucket_prefix='firstpythonbucket', 
      s3_connection=s3_resource.meta.client)


second_bucket_name, second_response = create_bucket(
  bucket_prefix='secondpythonbucket', s3_connection=s3_resource)


print(first_response)
print(second_response)
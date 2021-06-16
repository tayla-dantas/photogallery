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
        'LocationConstraint': 'sa-east-1'})
    print(bucket_name, 'sa-east-1')
    return bucket_name, bucket_response

def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name

first_bucket_name, first_response = create_bucket(
      bucket_prefix='firstpythonbucket', 
      s3_connection=s3_resource.meta.client)


second_bucket_name, second_response = create_bucket(
  bucket_prefix='secondpythonbucket', s3_connection=s3_resource)

first_file_name = create_temp_file(300, 'photo', 'f')   


first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)

first_object_again = first_bucket.Object(first_file_name)


first_bucket_again = first_object.Bucket()


print(first_response)
print(second_response)
print(first_file_name)

#### uploading photo

first_object.upload_file('tempPhotos/testPhoto.jpg')
print('first upload ok!')

s3_resource.meta.client.upload_file(
    Filename='tempPhotos/testPhoto.jpg', Bucket='secondpythonbucket08fd5c1c-a014-4245-a583-9733edac7f1c',
    Key='tempPhotos/testPhoto.jpg')
print('second upload ok!')





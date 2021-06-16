import boto3

s3_resource = boto3.resource('s3',aws_access_key_id='AKIASZ6M73INSE3WJPM4',
         aws_secret_access_key='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')

bucket = s3_resource.Bucket(name='galleryforafriend')

bucketObject = s3_resource.Object(
    bucket_name='galleryforafriend', 
    key='testPhoto.jpg'
)

bucketObject.upload_file('testPhoto.jpg')

print('upload ok!')
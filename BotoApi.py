import boto3, uuid, base64

_DEFAULT_BUCKET_NAME='galleryforafriend'
_DEFAULT_BUCKET_LOCATION='sa-east-1'

s3_resource = boto3.resource('s3',aws_access_key_id='AKIASZ6M73INSE3WJPM4',
         aws_secret_access_key='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')

bucket = s3_resource.Bucket(name=_DEFAULT_BUCKET_NAME)


def awsUpload(base64String): 
    FILE_NAME = str(uuid.uuid4()) + '.jpg'
    bucketObject = s3_resource.Object(
    bucket_name=_DEFAULT_BUCKET_NAME, 
    key=FILE_NAME)
    bucketObject.put(Body=base64.b64decode(base64String))
    #bucketObject.upload_file('testPhoto.jpg')
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (_DEFAULT_BUCKET_NAME,_DEFAULT_BUCKET_LOCATION, FILE_NAME)
    print(object_url)
    return 'upload ok'

def awsDownload():
    images = ()

    for bucketObject in bucket.objects.all():
        object_url = "https://%s.s3-%s.amazonaws.com/%s" % (_DEFAULT_BUCKET_NAME,_DEFAULT_BUCKET_LOCATION, bucketObject.key)
        #images.append(object_url)
        #images.add(object_url)
        imagesList = list(images)
        imagesList.append(object_url)
        images = tuple(imagesList)
    return images
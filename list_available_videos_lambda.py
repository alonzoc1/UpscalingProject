import json
import boto3
import os

BUCKET_NAME = "hidden"

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    return json.dumps(raw_to_result(s3.list_objects_v2(Bucket=BUCKET_NAME)))

def raw_to_result(raw):
    result = dict()
    location = raw["ResponseMetadata"]["HTTPHeaders"]["x-amz-bucket-region"]
    for obj in raw["Contents"]:
        if (obj['Key'].startswith('Library/') and os.path.basename(obj['Key']) != ""):
            name, new_result = create_video_object(location, obj['Key'])
            result[name] = new_result
    return result

def create_video_object(location, key):
    result = dict()
    result["url"] = construct_video_url(BUCKET_NAME, location, key)
    result["series"] = os.path.split(os.path.split(key)[0])[1]
    result["episode"] = os.path.split(key)[1] # In future keep track of this in metadata instead of just using filename
    name = os.path.basename(key)
    return (name, result)

def construct_video_url(bucket_name, bucket_location, key):
    url = "https://{0}.s3-{1}.amazonaws.com/{2}".format(
        bucket_name,
        bucket_location,
        key
    )
    return url

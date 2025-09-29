import boto3
import json


#Returns the 3 most recent files from S3 bucket
def list_recent_files(bucket, limit=3):
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket)

    if "Contents" not in response:
        return []

    # Sort by LastModified descending
    files = sorted(response["Contents"], key=lambda x: x["LastModified"], reverse=True)
    return [f["Key"] for f in files[:limit]]

#Gets the JSON file from S3 and return the content
def get_file(bucket, key):
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj["Body"].read().decode("utf-8")
    return json.loads(data)

#Upload the weather data for that city on that day on s3
def upload_to_s3(bucket, filename, data):
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=json.dumps(data),
        ContentType="application/json"
    )

import json
import base64
import boto3
import os

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract parameters from the event
        bucket_name = os.environ['S3_BUCKET_NAME']  # Use an environment variable for the bucket name
        file_content = event.get('file_content')   # Base64-encoded file content
        file_name = event.get('file_name')         # File name to save in the bucket
        
        if not file_content or not file_name:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: file_content and file_name are required.')
            }
        
        # Decode the base64-encoded file content
        file_data = base64.b64decode(file_content)
        
        # Upload the file to S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_data)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} successfully uploaded to bucket {bucket_name}.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

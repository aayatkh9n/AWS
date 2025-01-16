This repository contains two AWS Lambda functions:

Add Two Numbers - A Lambda function that takes two numbers, adds them, and returns the result.
Upload Document/PDF to S3 - A Lambda function that uploads a document or PDF file (in base64 encoding) to an S3 bucket.
Prerequisites
Before you begin, ensure that you have the following installed and set up:

AWS Account - You need an active AWS account to deploy these Lambda functions and access AWS resources such as S3.
AWS CLI - Install and configure the AWS CLI to interact with your AWS resources from your local machine.
Install AWS CLI
Boto3 - AWS SDK for Python, required for interacting with AWS services such as S3.
pip install boto3
Setup Instructions
1. Add Two Numbers Lambda Function
This Lambda function receives two numbers in the event and returns their sum.

Steps to Deploy:
Create Lambda Function:

Go to the AWS Lambda Console.
Click on "Create Function" and choose Python as the runtime.
Copy and paste the lambda_handler function from the add_two_numbers.py file into the inline code editor.
Create a Test Event:

Click on "Test" in the Lambda console.
Create a new test event with the following JSON structure:
json
Copy
Edit
{
  "num1": 5,
  "num2": 7
}
Click "Save and Test" to invoke the Lambda function.
IAM Role Permissions:

Ensure that the Lambda function has the appropriate IAM role with permissions to execute the function.
2. Upload Document/PDF to S3 Lambda Function
This Lambda function accepts a base64-encoded file and uploads it to an S3 bucket.

Steps to Deploy:
Set Up an S3 Bucket:

Create an S3 bucket in the AWS S3 console. Note the bucket name.
Create Lambda Function:

Go to the AWS Lambda Console.
Click on "Create Function" and choose Python as the runtime.
Copy and paste the lambda_handler function from the upload_to_s3.py file into the inline code editor.
Set Environment Variables:

Set the environment variable S3_BUCKET_NAME to the name of the S3 bucket you created.
Create a Test Event:

Click on "Test" in the Lambda console.
Create a new test event with the following JSON structure:
json
Copy
Edit
{
  "file_content": "base64-encoded-file-content",
  "file_name": "example.pdf"
}
Replace "base64-encoded-file-content" with the actual base64-encoded content of your file.
IAM Role Permissions:

Ensure that the Lambda function has an IAM role with permissions to upload files to the S3 bucket.
Example IAM policy to allow Lambda to upload files:
json
Copy
Edit
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
Running Locally
To test the Lambda functions locally, you can use the AWS SDK for Python (boto3) or mock the Lambda invocation by calling the handler function directly in a script.

Example to Test Add Two Numbers Function Locally:
Create a local test script (test_add_numbers.py):

python
Copy
Edit
from add_two_numbers import lambda_handler

event = {
    "num1": 5,
    "num2": 7
}

result = lambda_handler(event, None)
print(result)
Run the script:

bash
Copy
Edit
python test_add_numbers.py
Example to Test Upload Document to S3 Function Locally:
Create a local test script (test_upload_to_s3.py):

python
Copy
Edit
import base64
from upload_to_s3 import lambda_handler

with open("document.pdf", "rb") as file:
    encoded_content = base64.b64encode(file.read()).decode('utf-8')

event = {
    "file_content": encoded_content,
    "file_name": "uploaded_document.pdf"
}

result = lambda_handler(event, None)
print(result)
Run the script:

bash
Copy
Edit
python test_upload_to_s3.py
Troubleshooting
Invalid Permissions: Make sure your Lambda function has the correct IAM role permissions to access the necessary AWS resources, such as S3.
Incorrect Bucket Name: Double-check the bucket name in the environment variables or test events.
Base64 Decoding Issues: Ensure that the file content is properly base64-encoded before testing the "Upload Document to S3" function.
License
This project is licensed under the MIT License - see the LICENSE file for details.

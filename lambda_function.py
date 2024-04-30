import json
import logging
import requests

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  # Log event details
  logger.info(f"Received S3 event: {event}")

  # Get the S3 object information from the event
  s3_record = event['Records'][0]
  bucket_name = s3_record['s3']['bucket']['name']
  object_key = s3_record['s3']['object']['key']

  # Construct the public S3 object URL (for public buckets)
  public_url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

  # Prepare the payload
  payload = {
      "url": public_url
  }

  # Log payload details
  logger.info(f"Prepared payload: {payload}")

  try:
      response = requests.post(
          url='http://18.212.227.204/process',  # Replace with your external API URL
          headers={'Content-Type': 'application/json'},
          data=json.dumps(payload)
      )
      print(f"API response: {response.status_code}")
      print(f"API response content: {response.text}")  # Access response data
  except Exception as e:
      print(f"Error sending POST request: {e}")

  


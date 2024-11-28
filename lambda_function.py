import json
import time
from botocore.vendored import requests
import os

url = os.environ.get('url')

def lambda_handler(event, context):
    # Extract the callback URL and task parameters from the event (payload)
    task_data = event.get('task_data')
    callback_url = url+":8000/aws/webhook"

    # Simulate a long-running task (e.g., sending an email)
    print(f"Processing task: {task_data}")
    time.sleep(5)  # Simulate delay, e.g., sending an email

    # Prepare the response after task completion
    result = {
        "status": "success",
        "message": f"Task completed for {task_data}"
    }



    # Send the result back to the callback URL
    try:
        response = requests.post(callback_url, json=result)
        response.raise_for_status()  # Raise an error if the request fails
    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    # Return success to Lambda invocation
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task started successfully"})
    }

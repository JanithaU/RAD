from fastapi import APIRouter, Depends, HTTPException, status
from db.schema import TaskRequest
import boto3
import json
from core.config import settings
aws_router = APIRouter()


lambda_client = boto3.client("lambda", region_name="us-east-1")  # Specify your region


import os
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.region_name,
)


@aws_router.post("/webhook")
async def webhook(result: dict):
    # Process the result received from Lambda
    print(f"Received task result: {result}")
    # You can add further processing like notifying the user or logging the result
    return {"status": "received", "result": result}


@aws_router.post("/start-task")
async def start_task(request: TaskRequest):
    try:
        # Prepare the payload to pass to Lambda
        lambda_payload = {
            "data_dic": request.data,
            "task_data": request.task_data,
            "callback_url": request.callback_url
        }

        # Serialize the payload to JSON
        payload_bytes = json.dumps(lambda_payload).encode("utf-8")  # Proper JSON serialization

        # Invoke the Lambda function asynchronously
        response = lambda_client.invoke(
            FunctionName= settings.lambda_function,  # Your Lambda ARN
            InvocationType="Event",  # Asynchronous invocation
            Payload=payload_bytes,  # Pass serialized JSON payload
        )

        # Return a success message
        return {"message": "Task started successfully, you will be notified via callback URL.",
                "response":response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error starting task: {str(e)}")
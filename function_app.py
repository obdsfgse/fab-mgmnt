import azure.functions as func
import datetime
import json
import logging
import subprocess
import os
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential

app = func.FunctionApp()


# @app.function_name("FabAuthLogin")
# @app.route(route="fabric/auth/login", methods=["POST"])
# def fab_auth_login(req: func.HttpRequest) -> func.HttpResponse:
#     """
#     Authenticate with Fabric using the CLI with identity-based login,
#     then list workspace items with 'fab ls'.
#     Uses Azure Identity to retrieve credentials for user-assigned managed identity.
#     Expects JSON body with 'client_id' parameter (optional, will use default if not provided).
#     """
#     try:
#         req_body = req.get_json()
#         client_id = req_body.get("client_id")
#         credential = None
        
#         # Initialize Azure Identity credentials
#         try:
#             if client_id:
#                 # If client_id is provided, use ManagedIdentityCredential
#                 logging.info(f"Using provided client_id for managed identity")
#                 credential = ManagedIdentityCredential(client_id=client_id)
#                 logging.info(f"Successfully initialized ManagedIdentityCredential")
#             else:
#                 # Use DefaultAzureCredential which handles user-assigned managed identities
#                 logging.info("Retrieving Azure Identity credentials...")
#                 credential = DefaultAzureCredential()
#                 logging.info("Successfully obtained Azure Identity credential")
#         except Exception as e:
#             logging.error(f"Failed to obtain Azure Identity: {str(e)}")
#             return func.HttpResponse(
#                 json.dumps({
#                     "error": "Failed to obtain Azure Identity credentials",
#                     "details": str(e)
#                 }),
#                 status_code=401,
#                 mimetype="application/json"
#             )
        
#         # If still no client_id, we need one to pass to fab command
#         if not client_id:
#             logging.warning("No client_id available for fab command")
#             return func.HttpResponse(
#                 json.dumps({"error": "client_id is required or must be available via Azure Identity"}),
#                 status_code=400,
#                 mimetype="application/json"
#             )
        
#         # Step 1: Run fabric CLI auth login with identity
#         auth_cmd = [
#             "fab",
#             "auth",
#             "login",
#             "--identity",
#             "-u",
#             client_id
#         ]
        
#         logging.info(f"Executing: {' '.join(auth_cmd)}")
#         auth_result = subprocess.run(
#             auth_cmd,
#             capture_output=True,
#             text=True,
#             timeout=30
#         )
        
#         if auth_result.returncode != 0:
#             return func.HttpResponse(
#                 json.dumps({
#                     "status": "error",
#                     "message": "Authentication failed",
#                     "error": auth_result.stderr
#                 }),
#                 status_code=400,
#                 mimetype="application/json"
#             )
        
#         # Step 2: Run 'fab ls' to list workspace items
#         ls_cmd = ["fab", "ls"]
#         logging.info(f"Executing: {' '.join(ls_cmd)}")
#         ls_result = subprocess.run(
#             ls_cmd,
#             capture_output=True,
#             text=True,
#             timeout=30
#         )
        
#         if ls_result.returncode == 0:
#             return func.HttpResponse(
#                 json.dumps({
#                     "status": "success",
#                     "message": "Successfully authenticated and listed items",
#                     "auth_output": auth_result.stdout,
#                     "items": ls_result.stdout
#                 }),
#                 status_code=200,
#                 mimetype="application/json"
#             )
#         else:
#             return func.HttpResponse(
#                 json.dumps({
#                     "status": "error",
#                     "message": "Failed to list items",
#                     "auth_output": auth_result.stdout,
#                     "error": ls_result.stderr
#                 }),
#                 status_code=400,
#                 mimetype="application/json"
#             )
    
#     except json.JSONDecodeError:
#         return func.HttpResponse(
#             json.dumps({"error": "Invalid JSON in request body"}),
#             status_code=400,
#             mimetype="application/json"
#         )
#     except subprocess.TimeoutExpired:
#         return func.HttpResponse(
#             json.dumps({"error": "Command timed out"}),
#             status_code=408,
#             mimetype="application/json"
#         )
#     except Exception as e:
#         logging.error(f"Error: {str(e)}")
#         return func.HttpResponse(
#             json.dumps({"error": str(e)}),
#             status_code=500,
#             mimetype="application/json"
#         )


@app.function_name("Hello")
@app.route(route="hello", methods=["GET"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    """
    Simple hello endpoint to verify the function app is running.
    """
    logging.info("Hello endpoint was triggered")
    name = req.params.get("name")
    if not name:
        name = "World"
    
    return func.HttpResponse(
        json.dumps({
            "message": f"Hello, {name}!",
            "status": "success"
        }),
        status_code=200,
        mimetype="application/json"
    )
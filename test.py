import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {

    "question": "How can I request a refill for my prescription?",
    "chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://rag-2300-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyIsImtpZCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkxMzQ4MmI2LTEzMWEtNDQ5NC1iMzY3LTNlMzkyYmIwYzY4MC8iLCJpYXQiOjE3Mzg3NDkyNDEsIm5iZiI6MTczODc0OTI0MSwiZXhwIjoxNzM4NzU0NDA2LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFpBQUFBTzZrYWZSbXdseDJ5R0FHV0drZEtGWGw3R2REZlZ5Y0tCSWpJU3Y5UVN3WHZjdHZGQlBPbE56ODI1MmZhcE1SWVNxVG9GMlVCUVRBVWxJeDFqc1ZRRk1KZVd6bDI5aVp0UURXbVprd3hXZEk9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiQWRtaW5pc3RyYXRvciIsImdpdmVuX25hbWUiOiJNT0QiLCJncm91cHMiOlsiNjQ5ZDNjYWEtODg0Mi00ZTFhLWIyZjAtNjM2YTExYTEzNzQwIl0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE5NC4xNjYuMTQyLjIwMCIsIm5hbWUiOiJNT0QgQWRtaW5pc3RyYXRvciIsIm9pZCI6ImI4YjQwM2U4LTc5OGUtNDg0Ny05M2QxLTkwMTAwNjY1YWFiMiIsInB1aWQiOiIxMDAzMjAwNDQwNEIwQTAzIiwicmgiOiIxLkFXRUJ0b0kwa1JvVGxFU3paejQ1SzdER2dGOXZwaGpmMnhkTW5kY1dOSEVxbkw1aUFURmhBUS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzaWQiOiIwMDFmMjhhOS04OGU1LTdhNWYtZTMwNC1mNDU3YjczMzg3MDkiLCJzdWIiOiJDTHZKczBscjg1NXV1VXZHeFlBN3dDem9vc0F2dTg1V0JjR0hjQ0syeXpjIiwidGlkIjoiOTEzNDgyYjYtMTMxYS00NDk0LWIzNjctM2UzOTJiYjBjNjgwIiwidW5pcXVlX25hbWUiOiJhZG1pbkBNbmdFbnZNQ0FQODI0NDY3Lm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6ImFkbWluQE1uZ0Vudk1DQVA4MjQ0Njcub25taWNyb3NvZnQuY29tIiwidXRpIjoiWWNtRXBHcWFTMG0ybGQtd0UzM3RBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjEgMTQifQ.CfbvUTqTATxe4xS7_R7dOw6lyieGAQBx6JlwTwxB7-8mHb2fHsQf9a1N2QIRKOXXyus89MGAYeQWlOs5hMC6Y3jsi7Rwo8C5BcgCZUqOOnINUnZNQkhT3tmVVuLuq0iNM-vODRuiXDW4NfDfJwtzhUYRq9p_iqfff0lSpvv5TjW3v7Qm8-1XYO9w_Cp4JuO5_0yle6O54UyCCpMvbjzjoWbWXp1CkQzjXZP4TPWspiFl_qFV-3xXmQRyyPCVlQRISDspKPpSlfWTkZ_DI6OvFdvYA8ESgZz1J5_lB_p3kYQ_85EzgtCBE-JhAwglgcM8DohIFNTRdenvqDKHYJ6jVg'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/api/getdata', methods=['GET'])
def get_data():
    access_token = request.args.get('accessToken')
    if not access_token:
        return jsonify({"error": "Access token is required"}), 400  # Bad Request if no token is provided
    
    url = "https://catfact.ninja/fact"

    payload = {}
    headers = {
    'Cookie': '8EKCbfgSkXePBvY6IyF6KFfThGZ8snukUvFpwbW1=eyJpdiI6Ik12bTV4a1kwYTRCSnNvajI0L2VDRlE9PSIsInZhbHVlIjoib3JFTkpKRHhsU3k0ZGw5SVZCSWVldmw3Q3VSU21TUThnaWZxNW1OU3RSNFh3N3l6ZStSRXJiY2hkdnZad21xNnBYQ2tZMmowdEJRVUhVQkVxdXFyWkdjbklCbmlNQUNabGYrQVlQNnI5dmVBMkpxeERrU1lTMFdQbDUwUDRBcktoRTN6SEowcjM5UENRdnFvY1MvZXR3YUQ0ZEgwWDFCMWRlNGFHSUE2M1JQdjFVdHc0N052SFQ2ME15RW51V05FK2x4S0NHeFpRbFE1eUl3anlTa3pYQ3NmTk5TcnRhRzlXTHQxeGw1bkRaMjU1Nm5ZbmRxQ3lwRTVVUUNuY3g3TnZqZDVQWVNGZHVHZVIyK0tleml1aXpVa0VEUXBrVUxUQlhsK1lYcUJON25LNVpxcUUxTktmZSs4bDBMWVhvQVlIbVFMVms1UHNlVzV1N0FGR2prT3EvanlKd0tOSnVFZS9aQmFmRFJFakMzQ2w1TDdnTzk4VnNFMjZEbGkzWEJrIiwibWFjIjoiNWZlNTcxMGE1ZDJjYzQwM2IzNWNlZGQyMDZmZjU1YjM3NGU5N2U4N2I2NGRjNmMwYjk4NGE5M2E2YjY5OWRmYiIsInRhZyI6IiJ9; XSRF-TOKEN=eyJpdiI6IndQR09MODgrTm5xTys4REtaODg2NVE9PSIsInZhbHVlIjoia3YxMnFTM0s5TS9Bd3E2YmZmbGJ4UjlqcVUrU0VjMncyejl3YlBJK3MxeTl3WlEvNzh6dE94M3l3U2RFN3BXemJTYzBHZ08yeWNhakZPc01FYkhpb053ZHkwM2s3VzMvWkNFb1JQaTFiOXorb1NKZEd3Q2VkRzVzUVRDTGtFVzEiLCJtYWMiOiJjMjJmMjVhYjIwYWRiMTc3ODU4MjE0ODdjZmZhZGY5NDM3NDg4NTU5MTljN2U3NzYzNTMwMzVhY2E3OTcwN2ZkIiwidGFnIjoiIn0%3D; catfacts_session=eyJpdiI6IlIxZ3BEcHdWZjVNeSt6ZXRpWk9ySEE9PSIsInZhbHVlIjoiakNBVUEzaGwwa3QzUkpmay9DeCtGOWJnUHBmc0F6S0Q1bkxMWVc4UzRvWlZNcFVnN3VjMWFoMWJPenZEQ2gzRW5PYkVVeWlTNFVKTFRKZUhBcVBnYVNoc2IxNVFyYy9KTEZtU0dhdmc4eFd1cnFVWXIvK1FSWnJQRnAzMEllWG8iLCJtYWMiOiIyZGE4NmUwZTk3ZmQzMDE5MDI5MjllOGQxNjQ5ZGViMTJiMjlhNDhkMDE1ZjQ5YWE2NGY2OGZkOTQxOTc5ZjAzIiwidGFnIjoiIn0%3D'
    }

    


    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return jsonify(response.json())  # Return the JSON response from the API
    except requests.exceptions.HTTPError as err:
        app.logger.error(f"HTTPError: {err}, Response: {response.text}")  # Log the error
        return jsonify({"error": str(err), "response": response.text}), response.status_code
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")  # Log any other exceptions
        return jsonify({"error": "An unexpected error occurred."}), 500  # Internal Server Error

if __name__ == "__main__":
    app.run(debug=True)

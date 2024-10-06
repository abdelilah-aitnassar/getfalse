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
    
    url = "https://app.addtowallet.co/api/card/get?deleted=false"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'accessToken': access_token,  # Include the access token in the headers
        'Connection': 'keep-alive',
        'Referer': 'https://app.addtowallet.co/dashboard',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-None-Match': 'W/cf2-TqWDa+EvD6nexyBeysl55OTEwmQ',
        'TE': 'trailers'
    }

    try:
        response = requests.get(url, headers=headers)
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

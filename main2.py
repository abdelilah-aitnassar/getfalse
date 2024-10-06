from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_data', methods=['POST'])
def get_data():
    # Get the access token from the POST request
    access_token = request.json.get('accessToken')

    if not access_token:
        return jsonify({"error": "accessToken is required"}), 400

    url = "https://app.addtowallet.co/api/card/get?deleted=false"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'accessToken': access_token,  # Use the provided access token
        'Connection': 'keep-alive',
        'Referer': 'https://app.addtowallet.co/dashboard',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-None-Match': 'W/cf2-TqWDa+EvD6nexyBeysl55OTEwmQ',
        'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data", "status_code": response.status_code}), 500
    
    # Return the data in JSON format
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

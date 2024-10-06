from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define your API endpoint
@app.route('/api/getdata', methods=['GET'])
def get_data():
    access_token = request.args.get('accessToken')
    
    if not access_token:
        return jsonify({"error": "Access token is required"}), 400

    # Make the request using the provided access token
    url = "https://app.addtowallet.co/api/card/get?deleted=false"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'accessToken': access_token,  # Use the access token provided in the request
        'Connection': 'keep-alive',
        'Referer': 'https://app.addtowallet.co/dashboard',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        # Parse response as JSON
        data = response.json()
        return jsonify(data)  # Return the data from the external API
    except requests.exceptions.HTTPError as err:
        return jsonify({"error": str(err)}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Use the appropriate host and port

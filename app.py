from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/getdata', methods=['GET'])
def get_data():
    access_token = request.args.get('accessToken')
    
    if not access_token:
        return jsonify({"error": "Access token is required"}), 400

    url = "https://app.addtowallet.co/api/card/get?deleted=false"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/plain, */*',
        'accessToken': access_token,
    }

    try:
        response = requests.get(url, headers=headers)
        # Log the response status and content
        print(f"Response Status: {response.status_code}")
        print(f"Response Content: {response.text}")
        
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        return jsonify(data)
    except requests.exceptions.HTTPError as err:
        return jsonify({"error": str(err)}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

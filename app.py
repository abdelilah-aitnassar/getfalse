from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    url = "https://app.addtowallet.co/api/card/get?deleted=false"
    headers = {'accessToken': '0ed20556-4ce7-3f96-a79e-e3d37bc8c06b'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.HTTPError as err:
        return jsonify({"error": str(err)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)

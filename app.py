from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/getdata', methods=['GET'])
def get_data():
    # Get the access token from the query parameters
    access_token = request.args.get('accessToken', None)
    
    # Create a response with the access token
    response_data = {
        "accessToken": access_token,
        "message": "Access token received successfully!"
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)

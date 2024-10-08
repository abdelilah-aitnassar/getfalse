from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

def load_proxies(file_path):
    """Load the proxy list from a file."""
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]
    return proxies

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
        'accessToken': access_token,
        'Connection': 'keep-alive',
        'Referer': 'https://app.addtowallet.co/dashboard',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-None-Match': 'W/cf2-TqWDa+EvD6nexyBeysl55OTEwmQ',
        'TE': 'trailers'
    }

    proxies = load_proxies('proxies.txt')  # Load proxies from the file
    max_retries = 3  # Maximum number of retries for each proxy

    for proxy in proxies:
        for attempt in range(max_retries):
            try:
                # Define proxy settings
                proxy_dict = {
                    "http": proxy,
                    "https": proxy
                }

                # Make the request through the proxy
                response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=10)
                response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
                return jsonify(response.json())  # Return the JSON response from the API
            except requests.exceptions.HTTPError as err:
                app.logger.error(f"HTTPError: {err} for proxy: {proxy}")  # Log the error
                break  # Exit the retry loop if HTTPError occurs
            except requests.exceptions.ProxyError as err:
                app.logger.error(f"ProxyError: {err} for proxy: {proxy}")  # Log the proxy error
                if attempt < max_retries - 1:  # Wait before retrying
                    time.sleep(10)  # Wait for 10 seconds before retrying
            except Exception as e:
                app.logger.error(f"Unexpected error: {e} for proxy: {proxy}")  # Log any other exceptions
                break  # Exit the retry loop for unexpected errors

    return jsonify({"error": "All proxies failed to connect."}), 502  # Bad Gateway

if __name__ == "__main__":
    app.run(debug=True)

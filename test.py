from requests.exceptions import ConnectionError, Timeout, RequestException
from security import safe_requests

try:
    response = safe_requests.get("http://192.168.7.101", timeout=10)
    response.raise_for_status()  # Raise an error for HTTP codes >= 400
    print("Response received successfully")
except ConnectionError:
    print("Error: Unable to connect to the server. Connection was reset.")
except Timeout:
    print("Error: Request timed out. The server might be slow to respond.")
except RequestException as e:
    print(f"Error: An error occurred - {e}")

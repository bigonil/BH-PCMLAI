import requests

def get_access_token(base_url, username, password):
    """Authenticate and return an access token."""
    auth_url = f"{base_url}/session/login"
    response = requests.post(auth_url, json={"username": username, "password": password})
    response.raise_for_status()  # Raises an exception for HTTP errors
    return response.json()['token']

def export_data(base_url, token):
    """Make an API call to export data from Control-M."""
    export_url = f"{base_url}/data/export"  # Update with actual endpoint
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(export_url, headers=headers)
    response.raise_for_status()
    return response.json()  # Assuming the API returns JSON data

def main():
    base_url = 'https://your.controlm.server/api'  # Update with your actual Control-M API server
    username = 'your_username'
    password = 'your_password'

    try:
        # Authenticate and obtain an access token
        token = get_access_token(base_url, username, password)
        
        # Use the token to export data
        data = export_data(base_url, token)
        print("Exported Data:", data)
    
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred:", err)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
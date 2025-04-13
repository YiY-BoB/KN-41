import requests

def fetch_data():
    response = requests.get("https://api.github.com")
    return response.status_code

if __name__ == "__main__":
    print(fetch_data())

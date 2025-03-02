import json
import requests

config = None

def get_children():
    url = f"https://{config['SERVER_URL']}/{config['ACCOUNT_NAME']}"
    data = requests.get(url, headers={"Authorization": "Basic " + config["API_KEY"]})
    j_data = data.json()[config['ACCOUNT_NAME']]
    return j_data["children"]

if __name__ == "__main__":
    with open("ragic.config", "r") as f:
        config = json.load(f)
    print(get_children())

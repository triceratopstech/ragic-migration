import json
import requests

config = None

def get_tabs():
    url = f"https://{config['SERVER_URL']}/{config['ACCOUNT_NAME']}"
    data = requests.get(url, headers={"Authorization": "Basic " + config["API_KEY"]})
    j_data = data.json()[config['ACCOUNT_NAME']]
    return j_data["children"]

def get_tab_sheets(tab):
    return tab["children"]

if __name__ == "__main__":
    with open("ragic.config", "r") as f:
        config = json.load(f)
    tabs = get_tabs()
    print(get_tab_sheets(list(tabs.values())[2]))
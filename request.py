import requests
import os
def infoIP(ipAddress):
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ipAddress

    headers = {
        "Accept": "application/json",
        "x-apikey": os.environ.get("API_KEY")
    }

    response = requests.get(url, headers=headers)
    return response.text

export = infoIP
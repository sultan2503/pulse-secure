import requests

url = "https://35.170.39.58/api/v1/auth"

payload={}
headers = {
  'Authorization': 'Basic YXM6QXNAMTIz'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

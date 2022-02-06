import requests

url = "https://35.187.30.58/api/v1/auth"

payload={}
headers = {
  'Authorization': 'Basic YXM6QXNAMTIz'
#-- YXM6QXNAMTIz is combination of (username:password) with base64 encoding
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

#--Disable SSL: CERTIFICATE_VERIFY with verify=False

print(response.text)

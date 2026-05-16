import requests
#web page address 
url = "https://timesofindia.indiatimes.com/city/delhi/"
response = requests.get(url)
print(response.content)
import requests

url = input("Enter a URL: ")
response = requests.get(url)

if response.status_code == 200:
    print("Page content:")
    print(response.text)
else:
    print("Failed to retrieve the page.")
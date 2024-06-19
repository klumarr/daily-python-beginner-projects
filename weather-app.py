import requests

api_key = "b59bfb0f2d9f8d80b88875d550277171"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print("City not found.")
    print(f"Response Content: {response.content}")


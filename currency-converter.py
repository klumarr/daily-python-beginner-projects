import requests

api_key = "558d63abe88c40477c1910d1"
base_currency = input("Enter base currency (e.g. USD): ")
target_currency = input("Enter target currency (e.g. EUR): ")
amount = float(input("Enter amount to convert: "))

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rate = data['conversion_rates'][target_currency]
    converted_amount = amount * rate
    print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
else:
    print("Failed to retrieve exchange rate.")
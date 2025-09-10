import requests

def get_weather(city="New York"):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"☀️ {response.text} ")
    else:
        print("Failed to fetch the weather")

get_weather("Bronx")
get_weather("Brooklyn")
get_weather("Manhattan")
get_weather("Tarrytown")
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:    
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()


    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Request timed out: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None 

    else: 
        data = resp.json()

        return {
            "city": data["name"],
            "temp": data["main"]["temp"]
        }

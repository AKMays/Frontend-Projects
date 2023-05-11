import requests
import datetime
import json
from googletrans import Translator, LANGUAGES

def main():
    Name = input("Enter your name: ")

    translator = Translator()

    search_history = []

    Search_Count = 0
    while True:
        if Search_Count == 0:
            Option = input(f"""Hello {Name}, I am your Desktop Assistant! How may I help you?\n
                1. Check Weather
                2. Ask a Question
                3. Generate a Random Joke
                4. Get Current Time
                5. Translate Text
                6. Recent Searches
                7. Exit\n""")
            Search_Count += 1
        else:
            if Search_Count > 0:
                Option = input(f"""Hello {Name}, How else can I help?\n
                1. Check Weather
                2. Ask a Question
                3. Generate a Random Joke
                4. Get Current Time
                5. Translate Text
                6. Recent Searches
                7. Exit\n""")
                Search_Count += 1

        if Option == "1":
            city_name = input("Enter a city name: ")
            get_weather(city_name)
            search_history.append(f"Weather in {city_name}")  # Add this line to update the search history

        elif Option == "2":
            question = input("Ask me anything: ")
            api_key = "AIzaSyAmgvfYJ7YCnYrMqY4_YhuHnYQo2cdy-ow"  # Replace with your Google API key
            search_engine_id = "80e87a4757690442a"  # Replace with your Google Custom Search Engine ID
            max_results = 3  # Change this to the desired number of results to print
            results = search_google(question, api_key, search_engine_id)
            print_results(results, max_results)
            search_history.append(question)  # Add this line to update the search history

        elif Option == "3":
            joke = get_joke()
            print(joke)
            search_history.append(f"Random joke {joke}")  # Add this line to update the search history

        elif Option == "4":
            current_time = datetime.datetime.now()
            print(f"Current Time: {current_time}")
            search_history.append(f"Current Time {current_time}")

        elif Option == "5":
            text = input("Enter text to translate: ")
            print("Available languages:")
            for code, lang in LANGUAGES.items():
                print(f"{code}: {lang}")
            dest_lang = input("Enter destination language code: ")
            translation = translator.translate(text, dest=dest_lang)
            print(f"Translated text: {translation.text}")
            search_history.append(f"Translated from {LANGUAGES[translation.src]} to {LANGUAGES[dest_lang]}")  # Add this line to update the search history

        elif Option == "6":
                print(f"Recent searches {Search_Count}:")
                for search in search_history:
                    print("- " + search)

        elif Option == "7":
            print("Thank you for using the Desktop Assistant. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")


def search_google(query, api_key, search_engine_id):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"
    response = requests.get(url)
    data = response.json()
    return data.get('items', [])

def print_results(results, max_results=5):
    for i, result in enumerate(results[:max_results]):
        title = result.get('title', '')
        link = result.get('link', '')
        snippet = result.get('snippet', '')
        print(f"Result {i+1}:")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Description: {snippet}\n")

def get_weather(city_name):
    api_key = "74db2282467254dc0dbdcab2a10f59df"
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city_name}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extract relevant weather information from the API response
        location = data['location']['name']
        weather_info = data['current']['weather_descriptions'][0]
        temperature_c = data['current']['temperature']
        temperature_f = (temperature_c * 1.8) + 32

        print(f"Location: {location}")
        print(f"Weather: {weather_info}")
        print(f"Temperature in Celsius: {temperature_c}°C")
        print(f"Temperature in Fahrenheit: {temperature_f}°F")
    except Exception as e:
        print("An error occurred:", e)

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    return f"{data['setup']} {data['punchline']}"

main()

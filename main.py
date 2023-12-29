import speech_recognition as sr
import os
import pyttsx3
import webbrowser as web
import datetime
import wikipedia
import pywhatkit
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import requests

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me() :
    hour = datetime.datetime.now().hour
    if 0<=hour<12 :
        speak("Good Mourning")
    elif 12 <=hour < 18:
        speak("good afternoon")
    else:
        speak("Good Evening ")
    speak("I am Jarvis Sir. Please tell me how may i help you")
def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        speak("hmm")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"User Said : {query}")
        return query
    except Exception as e :
        print(f"Errore: {e}")
        return "error"

def open_website(url):
    speak(f"Opening{url} sir")
    web.open(url)

def My_Location():
    speak("Checking.....")
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/ip/geo' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    city = geo_d['city']
    state = geo_d['region']

    timezone = geo_d['timezone']
    country = geo_d['country']

    op = "https://www.google.com/maps/place/" + city
    web.open(op)

    print(f"sir, you are now in {city,state,country} and your time zone was {timezone}.")
    speak(f"sir, you are now in {city,state,country} and your time zone was {timezone}.")


    def GoogleMaps(place):
        Url_Place = "https://www.google.com/maps/place/" + str(place)
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(place , addressdetail = True)
        target_latlon = location.latitude , location.longitude
        web.open(url=Url_Place)
        location = location.raw['address']
        target = {'city' : location.get('city',''),
                  'state' : location.get('state',''),
                  'country' : location.get('country','')}  
                  
        current_loca = geocoder.ip('me')

        current_latlon = current_loca.latlng

        distance = str(great_circle(current_latlon, target_latlon))
        distance = str(distance.split('',1)[0])
        distance = str(round(float(distance),2))

        speak(target)
        speak(f"sir,{place} is {distance} kilometre away from your location.")


def main():

    speak("initializing jarvis")
    speak("all drivers are up and running")
    speak("all systems have been activated ")
    speak("now i am online ")
    speak("Hello, I am Jarvis")
    wish_me()
    while True:
        print("Listening.....")
        query = take_command().lower()

        if "open youtube" in query :
            open_website("https://www.youtube.com")
        elif "open google" in query : 
            open_website("https://www.google.com")
        elif "time" in query : 
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {current_time}")
        elif "wikipedia" in query : 
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "search youtube".lower() in query : 
            query = query.replace("search youtube ","")
            speak("searching Youtube for " + query)
            pywhatkit.playonyt(query)
            speak("I hope you find what you were looking for , Sir")
        elif "open in chrome".lower() in query.lower() :
            query = query.replace("open in chrome","")
            query = query.replace("jarvis","")
            speak("Searching for "+ query)
            open_website("https://www."+query)
        elif 'my locatin' in query : 
            My_Location()
        
        elif 'where is' in query : 
            Place = query.replace("where is","")
            Place = Place.replace("jarvis","")
            GoogleMaps(Place)
        
        elif "exit" in query :
            speak("Goodbye, Sir")
            exit()
        
if __name__ == "__main__" :
    main()
        


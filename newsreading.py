
#Newspaper reading ,source---newsapi.org

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=57e18f23794b41e39b01b176e9f5e8c5"

    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Next news is")
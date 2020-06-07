#!/usr/bin/python3
import time
from newsapi import NewsApiClient
from googletrans import Translator
# Init Provide your own API key here
newsapi = NewsApiClient(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
translator = Translator()
# /v2/top-headlines
top_headlines4 = newsapi.get_top_headlines(q='corona', page_size=5, country='in')
top_headlines3 = newsapi.get_top_headlines(q='corona', page_size=5, country='de')
top_headlines1 = newsapi.get_top_headlines(q='deutschland', country='de')
top_headlines2 = newsapi.get_top_headlines(q='india', page_size=20)
top_headlines5 = newsapi.get_top_headlines(q='business', language='en')
top_headlines6 = newsapi.get_top_headlines(q='science', language='en')
top_headlines7 = newsapi.get_top_headlines(q='kerala', language='en')

print('----------Germany headlines----------')
for i in top_headlines1['articles']:
    t1 = translator.translate([i['title'],i['description']])
    print(t1[0].text)
    print(t1[1].text)
    #print(i['description'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')
    #time.sleep(1)

print('----------India headlines----------')
for i in top_headlines2['articles']:
    print(i['title'])
    print(i['description'])
    #print(i['source'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')

print('----------Germany Corona----------')
for i in top_headlines3['articles']:
    t2 = translator.translate([i['title'],i['description']])
    print(t2[0].text)
    print(t2[1].text)
    #print(i['title'])
    #print(i['description'])
    #print(i['source'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')

print('----------India Corona----------')
for i in top_headlines4['articles']:
    print(i['title'])
    print(i['description'])
    #print(i['source'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')

print('----------Business headlines----------')
for i in top_headlines5['articles']:
    print(i['title'])
    print(i['description'])
    #print(i['source'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')

print('----------Science headlines----------')
for i in top_headlines6['articles']:
    print(i['title'])
    print(i['description'])
    #print(i['source'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')

print('----------Kerala headlines----------')
for i in top_headlines7['articles']:
    print(i['title'])
    print(i['description'])
    #print(i['source'])
    print(i['url'])
    #print(i['publishedAt'])
    print('\n')


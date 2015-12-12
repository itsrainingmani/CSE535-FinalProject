from textblob import TextBlob
import freqsummarizer
import ujson

def freqsum(text,n):
    fs = freqsummarizer.FrequencySummarizer()
    for s in fs.summarize(text,n):
        print '*',s

def sentiment(text):
    blob = TextBlob(text)
    print blob.sentiment

text1 = ""
with open('EnglishFinal.json','rb') as jsondata:
    tweets = ujson.load(jsondata)
    for tweet in tweets:
        text1 += tweet['text_en']

freqsum(text1,1)
sentiment(text1)

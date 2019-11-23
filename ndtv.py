import newspaper
from bs4 import BeautifulSoup
import nltk

ndtv = newspaper.build("https://www.ndtv.com/")

# print("FEEDS..")
# for feed in ndtv.feed_urls():
#     print(feed)                 #prints feed urls

# print("CATEGORY BASED URLS..")
# for category in ndtv.category_urls():                
#     print(category)                         # prints the categories of news

# print("BRAND: ")
# print(ndtv.brand)             #prints the name of the news website brand(name)  
# print("BRAND DESCRIPTION: ")   
# print(ndtv.description)       #prints today's categories of latest news

# print("ARTICLE URLS..")
# for article in ndtv.articles:
#     print(article.url)                                  #prints all the article urls
# print("No. of articles in today's paper",ndtv.size())




#Extracting article from newspaper
article = newspaper.Article("https://www.ndtv.com/entertainment/kalki-koechlin-on-her-unexpected-pregnancy-didnt-feel-any-maternal-instinct-in-first-two-months-2133932?pfrom=home-bollywood.html")
article.download()                                       #downoading the article
article.parse()
nltk.download('punkt')
article.nlp()
print("ARTICLE TEXT: ")
print(article.text)
print("ARTICLE SUMMARY: ")
print(article.summary)
print("ARTICLE KEYWORDS: ")
print(article.keywords)
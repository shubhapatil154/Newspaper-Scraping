import newspaper
from bs4 import BeautifulSoup
import nltk

dh = newspaper.build("https://www.deccanherald.com/")

# print("FEEDS..")
# for feed in dh.feed_urls():
#     print(feed)                 #prints feed urls

# print("CATEGORY BASED URLS..")
# for category in dh.category_urls():                
#     print(category)                         # prints the categories of news

# print("BRAND: ")
# print(dh.brand)             #prints the name of the news website brand(name)  
# print("BRAND DESCRIPTION: ") 
# print(dh.description)       

# print("ARTICLE URLS..")
# for article in dh.articles:
#     print(article.url)                                  #prints all the article urls
# print("No. of articles in today's paper",dh.size())




#Extracting article from newspaper
article = newspaper.Article("https://www.deccanherald.com/business/business-news/unnamed-buyer-to-take-20-737-max-planes-boeing-says-777773.html")
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
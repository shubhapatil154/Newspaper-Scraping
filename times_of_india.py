import newspaper
from bs4 import BeautifulSoup
import nltk

# print("FEEDS..")
# for feed in dc.feed_urls():
#     print(feed)                 #prints feed urls

# print("CATEGORY BASED URLS..")
# for category in dc.category_urls():                
#     print(category)                         # prints the categories of news


# print("BRAND: ")
# print(dc.brand)             #prints the name of the news website brand(name)  
# print("BRAND DESCRIPTION: ")
# print(dc.description)    

# print("ARTICLE URLS..")
# for article in toi.articles:
#     print(article.url)                 #prints all the article urls
                                   
# print("No. of articles in today's paper",toi.size())





toi = newspaper.build("https://www.timesofindia.indiatimes.com/")
#Extracting article from newspaper
article = newspaper.Article("http://economictimes.indiatimes.com/mf/best-mutual-funds-to-buy/top-mutual-fund-schemes-to-invest")
#downoading the article
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
print("ARTICLE TEXT: ")
print(article.text)
print("ARTICLE SUMMARY: ")
print(article.summary)
print("ARTICLE KEYWORDS: ")
print(article.keywords)
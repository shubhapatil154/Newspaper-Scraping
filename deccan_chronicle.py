import newspaper
from bs4 import BeautifulSoup
import nltk

dc = newspaper.build("https://www.deccanchronicle.com/")

# print("FEEDS..")
# for feed in dc.feed_urls():
#     print(feed)                 #prints feed urls

# print("CATEGORY BASED URLS..")
# for category in dc.category_urls():                
#     print(category)                         # prints the categories of news


# print("BRAND: ")
# print(dc.brand)             #prints the name of the news website brand(name)  
# print("BRAND DESCRIPTION: ")  
# print(dc.description)       #prints today's categories of latest news


# print("ARTICLE URLS..")
for article in dc.articles:
    print(article.url)                                  #prints all the article urls
print("No. of articles in today's paper",dc.size())




#Extracting article from newspaper
article = newspaper.Article("https://www.deccanherald.com/business/business-news/unnamed-buyer-to-take-20-737-max-planes-boeing-says-777773.html")
article.download()                                       #downoading the article
article.parse()
nltk.download('punkt')
article.nlp()
print("ARTICLE TEXT: ")
print(article.text)
print("ARTICLE AUTHOR: ")
print(article.authors)
print("ARTICLE SUMMARY: ")
print(article.summary)
print("ARTICLE IMAGES: ")
print(article.images)
print("ARTICLE KEYWORDS: ")
print(article.keywords)

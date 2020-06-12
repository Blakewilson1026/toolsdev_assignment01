import nltk
from newspaper import Article

#find article urls
articleURLs = ['https://www.gamespot.com/articles/heres-what-ps5-looks-like-playstation-5-design-rev/1100-6478306/', 
               'https://www.gamespot.com/articles/spiderman-miles-morales-announced-for-ps5/1100-6478314/',
               'https://www.gamespot.com/articles/call-of-duty-warzone-modern-warfare-patch-notes-fo/1100-6478276/']
articles = []

#create list of articles
for articleURL in articleURLs:
    articles.append(Article(articleURL))

#NLP 
nltk.download('punkt')
for article in articles:
    article.download()
    article.parse()
    article.nlp()

import nltk
import ssl
import newspaper
from newspaper import Article

#functions
def downloadPunkt():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('punkt')

# find news site urls
newsSites =  [newspaper.build('https://www.nytimes.com/' , memorize_articles=False),
              newspaper.build('https://www.foxnews.com/' , memorize_articles=False),
              newspaper.build('https://www.cnn.com/' , memorize_articles=False)]
#nyTimes_News = newspaper.build('https://www.nytimes.com/' , memorize_articles=False)

# ask users to enter keyword
print("Enter a keyword and press ENTER to search: ")
keyword = input()

# test nlp
#downloadPunkt()
#for article in nyTimes_News.articles:
#    print(article)
#    article.download()
#    article.parse()
#    article.nlp()
#    print(article.authors)

# NLP 
downloadPunkt()
for newsSite in newsSites:
    for article in newsSite.articles:
        article.download()
        article.parse()
        article.nlp()

    
# open file to write to
#newsSummary  = open('news_summary.txt', 'w')

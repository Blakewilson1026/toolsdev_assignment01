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
newsSites =  [newspaper.build('https://www.gamespot.com/news/' , memorize_articles=False),
              newspaper.build('https://www.pcgamer.com/news/' , memorize_articles=False),
              newspaper.build('https://www.gamesradar.com/news/' , memorize_articles=False)]
#gameSpot_News = newspaper.build('https://www.gamespot.com/news/' , memorize_articles=False)

# NLP 
downloadPunkt()
for newsSite in newsSites:
    for article in newsSite.articles:
        article.download()
        article.parse()
        article.nlp()

# ask users to enter keyword
print("Enter a keyword and press ENTER to search: ")
keyword = input()

# test output
if keyword in article.keywords:
    print(article.authors)
    
# open file to write to
#newsSummary  = open('news_summary.txt', 'w')

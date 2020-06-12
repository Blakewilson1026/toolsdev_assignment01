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
def printArticleInfo(article):
    print(str(article.title) + " -- " + str(article.authors))
    print(article.summary)
    print(" ")
def writeArticleInfoToFile(article,file):
    file.writelines(str(article.title) + " -- " + str(article.authors) + '\n')
    file.writelines(article.summary + '\n')
    file.writelines('\n')

# find news site urls
newsSites =  [newspaper.build('https://www.nytimes.com' , memoize_articles=False),
              newspaper.build('https://www.nbcnews.com/' , memoize_articles=False),
              newspaper.build('https://www.washingtonpost.com/' , memoize_articles=False)]
#nyTimes_News = newspaper.build('https://www.nytimes.com/' , memorize_articles=False)

# ask users to provide news site
print("Would you like to add a news source? (y/n)")
answer = input()
if answer == 'Y':
    answer = 'y'
if answer == 'y':
    print("Enter news URL: ")
    newNewsSite = input()
    newsSites.append(newspaper.build(newNewsSite , memoize_articles=False))


# ask users to enter keyword
print("Enter a keyword and press ENTER to search: ")
keyword = input()

# NLP and writing to file
downloadPunkt()
newsSummary = open('news_summary.txt' , 'w')
for newsSite in newsSites:
    for article in newsSite.articles:
        article.download()
        article.parse()
        article.nlp()
        if keyword == "":
            printArticleInfo(article)
            writeArticleInfoToFile(article, newsSummary)
        else:
            if keyword in article.keywords:
                printArticleInfo(article)
                writeArticleInfoToFile(article,newsSummary)
newsSummary.close()

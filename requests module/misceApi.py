# from newsapi import NewsApiClient;
# import requests;

# # Init
# newsapi = NewsApiClient(api_key='9b603a86fd3444a4b7326c3f0d6e60fd')

# #v2 country/category cannot mix with the sources 
# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           category='business',
#                                           language='en',
#                                           country='us')

#can only show result of one months 
# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-11-10',
#                                       to='2023-11-30',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# print(all_articles);

# /v2/top-headlines/sources
# sources = newsapi.get_sources()
# print(sources);

# key = '9b603a86fd3444a4b7326c3f0d6e60fd'
#https://newsapi.org/v2/everything?q=tesla&from=2023-10-30&sortBy=publishedAt&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd
#https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd
#https://newsapi.org/v2/top-headlines/sources?category=businessapiKey=API_KEY
#https://newsapi.org/v2/everything?q=tesla&from=2023-10-30&sortBy=publishedAt&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd
#https://newsapi.org/v2/everything?q=apple&from=2023-11-29&to=2023-11-29&sortBy=popularity&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd
#https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd
#https://newsapi.org/v2/everything?domains=wsj.com&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd

# url = 'https://newsapi.org/v2/everything?domains=ew.com&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd'
# r = requests.get(url);
# print(r);

# get_everything = newsapi.get_everything(domains='ew.com');

#json file lai format garera huge dictionary ascess garnai aayena

from newsapi import NewsApiClient
import requests;
import time;
from bs4 import BeautifulSoup;
import pprint;
import json;

# #get the current date from the time module 
# current_date = time.strftime('%Y-%m-%d');
# before = time.strftime('%Y-%m');
# #current date - 10 days 
# before_20 = int(time.strftime('%d'))-10;

# #if new month start it will give the serious problem
# if before_20 < 0:
#     before_20 = time.strftime('%m');

# #convert to string 
# before_20 = str(before_20);

# print(current_date, f'{before}-{before_20}');
# print(type(current_date), type(f'{before}-{before_20}'));

#types of news you can get
news = ['breaking news', 'buiseness', 'general', 'sports', 'music', 'health', 'technology', 'games', 'anime'];

string = '';
for i, str in enumerate(news):
    string = string + str.capitalize() + ', '; 

print('News Api'.capitalize().center(105, '-'));
print(f'''\nNews Api delivers the world current affairs in you home doors featuring several types news \nMembers can ascess this news : {string}only \nOur members can look headlines only \n''')

#run_news takes keyword and returns the domain to newsapi to fetch the news according to keyword and 
#provides the 5 news 
def run_news(keyword):

    #headlines news only take specified category so we have to limit the category at first
    headline = keyword;
    if headline == 'buiseness':
        category = 'buiseness';
    elif headline == 'sports':
        category = 'sports';
    elif headline == 'music':
        category = 'entertainment';
    elif headline == 'health':
        category = 'health';
    elif headline == 'technology':
        category = 'technology';
    elif headline == 'general':
        category = 'general'
    else:
        category = 'science';

    #run_headline fetch the headlines according to the category
    def run_headlines():
        top_headline = newsapi.get_top_headlines(q=headline,
                                                 category=category,
                                                 country='us',
                                                 language='en');
        
        #for loop used to show the title of the 10 news only
        for i, head in enumerate(top_headline['articles'][:10], 1):
            print(i, head['title'].upper());
    
    #keyword helps to fetch the all news because we cannot use the category class to get all news so 
    #keyword helps to give the domain for each category
    key = keyword;
    if key == 'breaking news':
        domain = 'foxnews.com';
    elif key == 'buiseness':
        domain = 'cnbc.com';
    elif key == 'anime':
        domain = 'cbr.com';
    elif key == 'sports':
        domain = 'cbssports.com';
    elif key == 'music':
        domain = 'ew.com';
    elif key == 'health':
        domain = 'medicalnewstoday.com';
    elif key == 'technology':
        domain = 'ycombinator.com';
    elif key == 'games':
        domain = 'gamespot.com';
    else:
        domain = 'msnbc.com'

    #Init the key from the news api
    newsapi = NewsApiClient(api_key='9b603a86fd3444a4b7326c3f0d6e60fd');
    get_everything = newsapi.get_everything(
                                        q=key,
                                        domains=domain,
                                        language='en',
                                        sort_by='relevancy',
    )

    # pprint.pprint(get_everything);

    for i in get_everything['articles'][:5]:
        print('\ntitle :', i['title'].upper());

        #none type has not the title() attribute so we have to put ifelse
        if i['author'] == None:
            print('author :', i['author']);
        else:
            print('author :', i['author'].title());
        print('content :',i['content']);
        print('url :',i['url']);
    
    #for headline ask user (y/n);
    for_headline = input('\nenter (y/n) for the headline :');
    if for_headline == 'y':
        run_headlines();
    else:
        print('Thankyou for using "news api"');

#ask from the user which news you want to read
keyWords = input('enter the keyword :');
if keyWords in news:
    run_news(keyWords);
else:
    print('sorry, use the above keyword carefully!');


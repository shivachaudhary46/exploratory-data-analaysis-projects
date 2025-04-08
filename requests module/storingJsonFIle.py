# urllib.request mostly for the http but requests can ascess through ssl and https
import urllib.request;
import json;

url = 'https://newsapi.org/v2/everything?domains=ew.com&apiKey=9b603a86fd3444a4b7326c3f0d6e60fd';

# #Initialize 
response = urllib.request.urlopen(url);

#we need to read the data and decode with the UTF-8
data = response.read().decode('UTF-8');

#make the empty json file
with open('data.json', 'w') as f:
    f.close();

#now load the json data which is in string convert with json.loads() to object
new_data = json.loads(data);
get_articles = new_data['articles'];

#convert specific articles data to the str
new_get_articles = json.dumps(get_articles); 

#now open the json file again
with open('data.json', 'w') as f:
    f.write(new_get_articles);
    f.close();
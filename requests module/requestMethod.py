import requests;
from bs4 import BeautifulSoup;
from requests.auth import HTTPBasicAuth;
# url = 'https://www.codewithharry.com/tutorial/cplusplus/';

# r = requests.get(url);
# print(r.text);

#get requests 
# url = 'https://www.codewithharry.com/tutorial/java/';
# r = requests.get(url);
# print('\n', r.text);

# #post request

# url = 'https://jsonplaceholder.typicode.com/posts';
# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# data = {
#     'id': 12,
#     "title": 'hahahhahha....',
#     "body": 'i have many sexy body parts',
#     "userId": 101
# }

# response = requests.post(url, headers=headers, json=data);
# print(response.text);

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)

#get post
# url = 'https://replit.com/@yuukiaasuna100/89-Day-89-Requests-Module#main.py'; 

# response = requests.get(url);
# # print(response.text);

# #syntax = beautifulSoup(from url text , 'html.parser');
# soup = BeautifulSoup(response.text, 'html.parser');
# # print(soup.prettify());

# for heading in soup.find_all('h2'):
#     print(heading);

# for script in soup.find_all('script'):
#     print(script);

#how to post request in the 
# url = 'https://jsonplaceholder.typicode.com/posts'
# header = {'Content-type': 'application/json; charset=UTF-8',};
# data = {'title':'foo...', 'body':'see ya', 'userId':202};
# response = requests.post(url, headers=header, json=data);
# print(response.text);

# url = "https://api.example.com/login"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Content-Type": "application/json"
# }
# data = {
#     "username": "myusername",
#     "password": "mypassword"
# }
# response = requests.post(url, headers=headers, json=data)
# print(response.text)

# url = 'https://www.geeksforgeeks.org/python-requests-tutorial/';
# r = requests.get(url);
# print(r.status_code);

# #header show content type , charser = encoding element
# # print(r.headers);
# #response.encoding returns the encoding used to decode response.content.
# print(r.encoding);
# # print(r.text);
# print(r.json);

# # print(r.data);
# soup = BeautifulSoup(r.content, 'html.parser');
# # print(soup.prettify());

# #returns the time from sending the request to arrival of the response
# print(r.elapsed);

# #response.cookies returns a CookieJar object with the cookies sent back from the server
# print(r.cookies);

# #response.history returns a list of response objects holding the history of request (url)
# print(r.history);

# #response.is_permanent_redirect returns True if the response is the permanent redirected url, otherwise False.
# print(r.is_permanent_redirect);

# #response.iter_content() iterates the content
# # r.iter_content();

# print(r.url);

# #response.request returns the request object that requested this response.
# print(r.request);

# #response.ok returns True if status_code is less than 200, otherwise False.
# print(r.ok);

# #response.raise_for_status() returns an HTTPError object if an error has occurred during the process.
# # r.raise_for_status();

# #response.links returns the header links.
# print(r.links);


#dont know the username and password
# # Making a get request 
# response = requests.get('https://api.github.com / user, ', 
#             auth = HTTPBasicAuth('username', 'password')) 
# # print request object 

#request module can gets acsess the ssl certificate verification website if cannot ascees it throws ssl error
url = 'https://www.kaspersky.com/resource-center/definitions/what-is-a-ssl-certificate';


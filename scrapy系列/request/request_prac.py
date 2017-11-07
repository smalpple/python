import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.shiyanlou.com/").text
soup = BeautifulSoup(response,'html.parser')
coursee = soup.find_all('div',{'class':'col-md-4','class':'col-sm-6','class':'course'})
print(coursee)
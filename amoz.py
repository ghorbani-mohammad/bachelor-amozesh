import requests
from bs4 import BeautifulSoup
import urllib.request

url_captcha="http://golestan.araku.ac.ir/home/balancer/balancer.aspx?vv=2&cost=main"
url_captcha_img="http://golestan.araku.ac.ir/home/balancer/captcha.aspx"

s=requests.session()
r=s.get(url_captcha)


soup = BeautifulSoup(r.text, 'html.parser')

VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


# print(r.cookies)
# print(r.cookies['ASP.NET_SessionId'])
SessionId=r.cookies['ASP.NET_SessionId']
print(r.status_code)
# print(r.cookies.get_dict("ASP.NET_SessionId"))
# print(r.text)
# print(s.headers)
r=s.get("http://golestan.araku.ac.ir/home/balancer/captcha.aspx")
print(r.status_code)
print(r.text)
# print(s.headers)
print(r.headers)

urllib.request.urlretrieve("http://golestan.araku.ac.ir/home/balancer/captcha.aspx","captcha.jpg")
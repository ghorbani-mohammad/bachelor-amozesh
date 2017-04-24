import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import re


url_captcha="http://golestan.araku.ac.ir/home/balancer/balancer.aspx?vv=2&cost=main"
url_captcha_img="http://golestan.araku.ac.ir/home/balancer/captcha.aspx"

s=requests.session()
r=s.get(url_captcha)

img_raw=s.get(url_captcha_img)
img_byte=BytesIO(img_raw.content)
img=Image.open(img_byte)
img.save('captcha.jpg')


# urllib.request.urlretrieve(url_captcha_img,"captcha.jpg")


soup = BeautifulSoup(r.text, 'html.parser')
#
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


# print(r.cookies)
# print(r.cookies['ASP.NET_SessionId'])
# SessionId=r.cookies['ASP.NET_SessionId']





#
s.headers.update({'Referer': 'http://golestan.araku.ac.ir/home/balancer/balancer.aspx?vv=2&cost=main'})
s.headers.update({'Accept': 'text/html, application/xhtml+xml, */*'})
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'})
#
s.cookies.update({'su':'','ft':'','f':'','seq':''})

# print(s.headers)
# print(s.cookies)

captcha=input('Please Insert Captcha:')
#
r=s.post(url_captcha,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'hip':captcha})
#
# print(r.status_code)
# print(r.text)
# print(r.headers)
text=r.content

# text=text.decode('utf-8')

# print(text)
# print(r.content.decode('utf-8'))
# text=r.content
#
# result=re.search(b'\'(.*)\'', text)
# # result=re.search(b'setcid.aspx?cid=(.*)</script>', text)
# text=result.group(0)[0]
# print(text)
# text=result.group(1)[0]
# print(text)


# start='<sc'
#
# print s[s.find(start)+len(start):s.rfind(end)]



start=text.find(b'<script>')+len('<script>')
end=text.find(b'</script>')
print(text[start:end])


start=text.find(b'setcid.aspx?cid')+len('setcid.aspx?cid')
end=text.find(b'</script>')-3
print(text[start+1:end])


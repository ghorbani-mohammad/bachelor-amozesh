import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import re


url_captcha="http://golestan.araku.ac.ir/home/balancer/balancer.aspx?vv=2&cost=main"
url_captcha_img="http://golestan.araku.ac.ir/home/balancer/captcha.aspx"
url_set_cid="https://golestan.araku.ac.ir/Forms/AuthenticateUser/setcid.aspx?cid"

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



# start=text.find(b'<script>')+len('<script>')
# end=text.find(b'</script>')
# print(text[start:end])


start=text.find(b'setcid.aspx?cid')+len('setcid.aspx?cid')
end=text.find(b'</script>')-3
cid=text[start:end]
cid=cid.decode()
# print(cid)

# print(url_set_cid+cid)
r=s.get(url_set_cid+cid,verify=False)

# print(r.status_code)
# print(r.text)
# print(r.content)

s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/AuthenticateUser/login.htm'})
r=s.get('https://golestan.araku.ac.ir/Forms/AuthenticateUser/login.htm')

s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/AuthenticateUser/nav.htm?fid=0;1&tck=&'})
r=s.get('https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.aspx?fid=0;1&tck=&')




# print(r.status_code)
# print(r.content)
# print(r.headers)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
#
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


url_Post_UserPass=soup.find(id="DataModi").get('action')
url_Post_UserPass=url_Post_UserPass[1:]
url_Post_UserPass='https://golestan.araku.ac.ir/Forms/AuthenticateUser'+url_Post_UserPass


User='9213231259'
Pass='zXc@#$zXc73'

User_Pass='<r F51851="" F80401="'+Pass+'" F80351="'+User+'" F83181="" F51701=""/>'
# s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/AuthenticateUser/AuthUser.aspx?fid=0%3b1&tck=&&&lastm=20170220062406'})
r=s.post(url_Post_UserPass,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'TxtMiddle':User_Pass,'Fm_Action':'09','Frm_Type':'','Frm_No':'','TicketTextBox':''})


# print(r.content)
# print(r.text)

cookie=r.headers['Set-Cookie']
# print(cookie)

start=cookie.find('stdno=')+len('stdno=')
end=cookie.find('; expires')
stdno=cookie[start:end]
cookie=cookie[end+len('; expires'):]
# print(stdno)
# print(cookie)

start=cookie.find('u=')+len('u=')
end=cookie.find('; path=/; Http')
u=cookie[start:end]
cookie=cookie[end+len('; path=/; Http'):]
# print(u)
# print(cookie)

start=cookie.find('lt=')+len('lt=')
end=cookie.find('; path=/; Http')
lt=cookie[start:end]
# print(lt)

# text=r.content
# print(len(text))
# start=text.find(b'showusr')+len('showusr')
# print(start)
# end=text.find(b'SetUsr')
# print(end)
# cid=text[start:end]
# print(cid)
# cid=cid.decode()
# print(cid)





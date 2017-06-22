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


soup = BeautifulSoup(r.text, 'html.parser')

VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


s.headers.update({'Referer': 'http://golestan.araku.ac.ir/home/balancer/balancer.aspx?vv=2&cost=main'})
s.headers.update({'Accept': 'text/html, application/xhtml+xml, */*'})
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'})
s.cookies.update({'su':'','ft':'','f':'','seq':''})


captcha=input('Please Insert Captcha:')
r=s.post(url_captcha,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'hip':captcha})
text=r.content


start=text.find(b'setcid.aspx?cid')+len('setcid.aspx?cid')
end=text.find(b'</script>')-3
cid=text[start:end]
cid=cid.decode()

r=s.get(url_set_cid+cid,verify=False)

s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/AuthenticateUser/login.htm'})
r=s.get('https://golestan.araku.ac.ir/Forms/AuthenticateUser/login.htm')

s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/AuthenticateUser/nav.htm?fid=0;1&tck=&'})
r=s.get('https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.aspx?fid=0;1&tck=&')


soup = BeautifulSoup(r.text, 'html.parser')


VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')


url_Post_UserPass=soup.find(id="DataModi").get('action')
url_Post_UserPass=url_Post_UserPass[1:]
url_Post_UserPass='https://golestan.araku.ac.ir/Forms/AuthenticateUser'+url_Post_UserPass


User='9213231259'
Pass='zXc@#$zXc73'

User_Pass='<r F51851="" F80401="'+Pass+'" F80351="'+User+'" F83181="" F51701=""/>'
r=s.post(url_Post_UserPass,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'TxtMiddle':User_Pass,'Fm_Action':'09','Frm_Type':'','Frm_No':'','TicketTextBox':''})

cookie=r.headers['Set-Cookie']


start=cookie.find('stdno=')+len('stdno=')
end=cookie.find('; expires')
stdno=cookie[start:end]
cookie=cookie[end+len('; expires'):]

start=cookie.find('u=')+len('u=')
end=cookie.find('; path=/; Http')
u=cookie[start:end]
cookie=cookie[end+len('; path=/; Http'):]

start=cookie.find('lt=')+len('lt=')
end=cookie.find('; path=/; Http')
lt=cookie[start:end]

seq=r.content
start=seq.find(str.encode(lt+"','"+lt))+len(lt+"','"+lt)
end=seq.find(str.encode('ورود به سيستم'))
seq=seq[start+2:end-2]
seq=seq.decode()

s.cookies.update({'seq':seq,'su':'0','f':'1','ft':'0'})
s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/AuthenticateUser/main.htm'})
url="https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.htm?r=0.49174303911660877&fid=0;11130&b=&l=&tck="+lt
r=s.get(url)


s.cookies.update({'seq':seq,'su':'0','f':'1','ft':'0'})
s.headers.update({'Referer': 'https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.htm?r=0.4917430391166087&fid=0;11130&b=&l=&tck='+lt})
url='https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav_Mai.htm'
r=s.get(url)



s.headers.update({'Referer': 'https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.htm?r=0.49174303911660877&fid=0;11130&b=&l=&tck='+lt})
url="https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.aspx?r=0.49174303911660877&fid=0;11130&b=&l=&tck="+lt
r=s.get(url)



seq=r.content
start=seq.find(str.encode(lt))+2*len(lt)
end=seq.find(str.encode('منوي كاربر'))
seq=seq[start+5:end-2]
seq=seq.decode()

soup = BeautifulSoup(r.text, 'html.parser')
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')
TicketTextBox=soup.find(id="TicketTextBox").get('value')


s.cookies.update({'seq':seq,'su':'0','f':'11130','ft':'0'})
s.headers.update({'Referer': 'https://golestan.araku.ac.ir/Forms/F0213_PROCESS_SYSMENU/F0213_01_PROCESS_SYSMENU_Dat.aspx?r=0.33257199920332586&fid=0;11130&b=&l=&tck='+lt+'&&lastm=20090829075642'})
url='https://golestan.araku.ac.ir/Forms/F0213_PROCESS_SYSMENU/F0213_01_PROCESS_SYSMENU_Dat.aspx?r=0.33257199920332586&fid=0%3b11130&b=&l=&tck='+lt+'&&lastm=20090829075642'
r=s.post(url,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'Fm_Action':'00','Frm_Type':'','Frm_No':'','TicketTextBox':TicketTextBox,'XMLStdHlp':'','TxtMiddle':'<r/>'})


content=r.content
start=content.find(str.encode(lt))+len(lt)
lt_copy=lt
lt=content[start+3:start+len(lt)+3]
lt=lt.decode()


#
s.cookies.update({'seq':seq,'su':'0','f':'11130','ft':'0'})
s.headers.update({'Referer': 'https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.htm?r=0.6707888345168351&fid=0;12310&b=0&l=0&tck='+lt})
url='https://golestan.araku.ac.ir/forms/f0240_process_authnav/nav.aspx?r=0.6707888345168351&fid=0;12310&b=0&l=0&tck='+lt
r=s.get(url)


seq=r.content
start=seq.find(str.encode(lt_copy))+2*len(lt_copy)
end=seq.find(str.encode('اطلاعات جامع دانشجو'))
seq=seq[start+5:end-2]
seq=seq.decode()


soup = BeautifulSoup(r.text, 'html.parser')
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')
TicketTextBox=soup.find(id="TicketTextBox").get('value')


s.cookies.update({'seq':seq,'su':'3','f':'12310','ft':'0'})
s.headers.update({'Referer':'https://golestan.araku.ac.ir/Forms/F1802_PROCESS_MNG_STDJAMEHMON/F1802_01_PROCESS_MNG_STDJAMEHMON_Dat.aspx?r=0.6707888345168351&fid=0;12310&b=0&l=0&tck='+lt+'&&lastm=20140622082604'+lt})
url='https://golestan.araku.ac.ir/Forms/F1802_PROCESS_MNG_STDJAMEHMON/F1802_01_PROCESS_MNG_STDJAMEHMON_Dat.aspx?r=0.6707888345168351&fid=0%3b12310&b=0&l=0&tck='+lt+'&&lastm=20140622082604'
r=s.post(url,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'Fm_Action':'00','Frm_Type':'','Frm_No':'','TicketTextBox':TicketTextBox,'XMLStdHlp':'','TxtMiddle':'<r/>'})


soup = BeautifulSoup(r.text, 'html.parser')
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')
TicketTextBox=soup.find(id="TicketTextBox").get('value')

#
s.cookies.update({'seq':seq,'sno':'9213231259','stdno':'9213231259','su':'3','f':'12310','ft':'0'})
url='https://golestan.araku.ac.ir/Forms/F1802_PROCESS_MNG_STDJAMEHMON/F1802_01_PROCESS_MNG_STDJAMEHMON_Dat.aspx?r=0.6707888345168351&fid=0%3b12310&b=0&l=0&tck='+lt+'&&lastm=20140622082604'
r=s.post(url,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':'6AC8DB9B',
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'Fm_Action':'08','Frm_Type':'','Frm_No':'','TicketTextBox':TicketTextBox,'XMLStdHlp':'','TxtMiddle':'<r F41251="9213231259"/>'})




soup = BeautifulSoup(r.text, 'html.parser')
VIEWSTATE=soup.find(id="__VIEWSTATE").get('value')
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR").get('value')
EVENTVALIDATION=soup.find(id="__EVENTVALIDATION").get('value')
TicketTextBox=soup.find(id="TicketTextBox").get('value')


s.cookies.update({'seq':seq,'sno':'9213231259','stdno':'9213231259','su':'3','f':'12310','ft':'0'})
url='https://golestan.araku.ac.ir/Forms/F1802_PROCESS_MNG_STDJAMEHMON/F1802_01_PROCESS_MNG_STDJAMEHMON_Dat.aspx?r=0.6707888345168351&fid=0%3b12310&b=0&l=0&tck='+lt+'&&lastm=20140622082604'
r=s.post(url,data={'__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':'6AC8DB9B',
                                        '__EVENTVALIDATION':EVENTVALIDATION,
                                        'Fm_Action':'80','Frm_Type':'','Frm_No':'','TicketTextBox':TicketTextBox,'XMLStdHlp':'','TxtMiddle':'<r F41251="9213231259" F43501="3952"/>'})

content=r.content
start=content.find(str.encode('<Root>'))
start=start+len('<Root>')
end=content.find(str.encode('</Root>'))
end=end+len('</Root>')
content2=content[start:end]
content2=content2.decode()

content=r.content[end:]
start=content.find(str.encode('<Root>'))
start=start+len('<Root>')
end=content.find(str.encode('</Root>'))
end=end+len('</Root>')
content2=content[start:end]

content=content2

id = content.find(str.encode('id="'))
while id != -1:
    id = content.find(str.encode('id="'))
    end = id + len('id="')
    content = content[end:]

    stOfCourse = content.find(str.encode('F0200="'))
    stOfCourse = stOfCourse + len('F0200="')
    enOfCourse = content.find(str.encode('" F0205="'))

    stGrOfCourse = content.find(str.encode('F3945="'))
    stGrOfCourse = stGrOfCourse + len('F3945="')
    enGrOfCourse = content.find(str.encode('" F3955="'))

    print(content[stOfCourse:enOfCourse].decode() + ": " + content[stGrOfCourse:enGrOfCourse].decode())
    id = content.find(str.encode('id="'))
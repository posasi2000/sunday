# 11bs.py  =  BeautifulSoup기술 접근

from bs4 import BeautifulSoup
import time

html_doc = """<html><head><title> webtest - 고희동 </title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">... webtest - class=story </p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify()) #권장
# print()
# time.sleep(1)
# print()

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print()

print(soup.title.parent.name)
print()
print(soup.p)
print(soup.p['class'])
print()
print('🎊 '  * 30  )


print(soup.a) #첫번째꺼 한건만
print()
print(soup.find_all('a')) #리스트
print()
print(soup.find(id="link3") )
print()

print('for반복문 a태그 <a href=~~> 출력')
for link in soup.find_all('a'):
    print(link.get('href'))

print()
print('~ ' * 50)
print(soup.get_text())#태그tag정보빠지고 내용만 함수로 접근
print('~ ' * 50)
print(soup.get_text) #태그tag정보까지 출력 속성로 접근 

# 참고 bs설치  pip install beautifulsoup4
# 참고 bs설치  pip install lxml


time.sleep(1)
print()
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment)
print(type(comment))
print('참고참고 각자 연습 https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' http://py4e-data.dr-chuck.net/known_by_Heidar.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0

# Retrieve all of the hyperlinks in the pages and enter the 18th url for 6 times
while count < 6:
	tags = soup('a')
	media = []
	for tag in tags:
		media.append(tag.get('href', None))
	url = media[17]
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	count = count + 1

# Get and print the tag of the 18th hyperlink
if count == 6:
	tags = soup('a')
	media = []
	for tag in tags:
		media.append(tag)
	result = str(media[17])
	final_result = re.findall('^<.+>(\S+)</a>$', result)

print(final_result.pop())

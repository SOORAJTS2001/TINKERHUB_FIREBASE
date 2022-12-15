import requests
from bs4 import BeautifulSoup
choice = input("enter the topic you want to scrap")
response = requests.get(
	url=f"https://en.wikipedia.org/wiki/{choice}",
)
soup = BeautifulSoup(response.content, 'html.parser')
ans = []
title = soup.find(id="firstHeading")
for data in soup.find_all("p"):
    ans.append(data.get_text())
print(title.string)
# the index of two is used because sometimes a newline or heading would come before that
print(ans[2])

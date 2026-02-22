from bs4 import BeautifulSoup
import requests

input_url = "https://www.icc-cricket.com/tournaments/mens-t20-world-cup-2026/matches"

response = requests.get(input_url)
print(response.status_code)

bs = BeautifulSoup(response.content,'html.parser')

if bs.title:
    print("TITLE: " + bs.title.get_text().strip() + "\n")
else:
    print("No title found\n")

if bs.body:
    print("BODY: " + bs.body.get_text().strip() + "\n")
else:    
    print("No body found\n")

print("URLs:\n")
if bs.find_all('a'):
    for t in bs.find_all('a'):
        href = t.get("href")
        if href:
            print(href)
else:
    print("No URLs found\n")

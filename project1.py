from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) < 2:
    print("<URL>")
    sys.exit()

input_url = sys.argv[1]

response = requests.get(input_url)
print(response.status_code)

bs = BeautifulSoup(response.content,'html.parser')

if bs.title:
    print(bs.title.get_text().strip())
else:
    print("No title found\n")

if bs.body:
    print(bs.body.get_text().strip())
else:    
    print("No body found\n")

if bs.find_all('a'):
    for t in bs.find_all('a'):
        href = t.get("href")
        if href:
            print(href)
else:
    print("No URLs found\n")

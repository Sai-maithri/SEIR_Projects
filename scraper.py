from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

def parse_url(input_url):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(input_url)
    time.sleep(2)

    html = driver.page_source
    driver.quit()

    bs = BeautifulSoup(html, 'html.parser')

    if bs.title:
        print(bs.title.get_text().strip())
    else:
        print("No title found")

    if bs.body:
        print(bs.body.get_text().strip() )
    else:
        print("No body found")

    if bs.find_all('a'):
        for t in bs.find_all('a'):
            href = t.get("href")
            if href:
                print(href)
    else:
        print("No URLs found")              

def main():
    if len(sys.argv) < 2:
        print("URL:")
        sys.exit()
    else:
        input_url = sys.argv[1]
        if not input_url.startswith("https://") or input_url.startswith("http://"):
            parse_url("https://" + input_url)
        else:
            parse_url(input_url)

if __name__ == "__main__":
    main()
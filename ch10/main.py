import requests
from bs4 import BeautifulSoup



def main():
    r = requests.get("https://logs.eolem.com")
    soup = BeautifulSoup(r.text, 'html.parser')
    list_a = soup.find_all('a')
    for a in list_a:
        print(a.text)


if __name__ == '__main__':
    main()
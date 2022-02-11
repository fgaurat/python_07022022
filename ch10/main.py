import requests
from bs4 import BeautifulSoup
import glob

def main():
    logs = sorted(glob.glob('*.log'))
    print(logs)

def main_download():
    r = requests.get("https://logs.eolem.com")
    soup = BeautifulSoup(r.text, 'html.parser')
    list_a = soup.find_all('a')
    for a in list_a:
        # print(a.get('href'))
        if '.log' in a['href']:
            with open(a['href'],'w') as f:
                r = requests.get(f'https://logs.eolem.com/{a["href"]}')
                print(r.text,file=f)


if __name__ == '__main__':
    main()
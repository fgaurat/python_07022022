import requests
from bs4 import BeautifulSoup
import glob
import re

def main():
    logs = sorted(glob.glob('*.log'))
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                # result = re.findall(r'((\d{1,3}\.){3}\d{1,3})',line)
                result = re.findall(r'^(.+?)\s',line)
                result_404 = re.findall(r'"\s404',line)
                if len(result_404)>0:
                    print(result)
                    print(result_404)


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
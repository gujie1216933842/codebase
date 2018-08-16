import requests
import re


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        return None


def main():
    url = 'http://maoyan.com/board/4?offset=40'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()

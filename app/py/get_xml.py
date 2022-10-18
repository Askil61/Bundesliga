from bs4 import BeautifulSoup
import lxml
import requests

class UrlNotFound(BaseException):
    e_message = "cannot open url"
    ...

def get_urls(main_url: str, paths: list[str]) -> list[str]:
    urls = []

    for idx, path in enumerate(paths):
        urls.append(main_url + path)

    return urls


def get_xml(url: str = "") -> BeautifulSoup:

    r:requests.Response = requests.get(url)

    if r.status_code == 200:
        content = r.content
        return BeautifulSoup(content, "lxml-xml")
    raise UrlNotFound



if __name__ == '__main__':
    print(get_xml("https://www.welt.de/feeds/ooh/out-of-home/bundesliga/news").prettify())

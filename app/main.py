import os
from typing import Any

from py.write_file import write_xml_file
from py.get_xml import UrlNotFound, get_xml, get_urls
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from py.reconst_xml import get_highlights, get_news

load_dotenv()

class EnvNotFound(BaseException):
    e_message = ".env var not found or var in .env not found"
    ...

def main():

    # xml from web import
    # from https://www.welt.de/feeds/ooh/out-of-home/bundesliga/highlights

    url: str | None = os.getenv("URL_BL")
    # holds xml data from urls
    xml_data = {"highlights": Any, "news": Any}
    xml_funcs = [get_highlights, get_news]

    if url is not None:
        urls = get_urls(url, list(xml_data.keys()))
    else:
        raise EnvNotFound

    for idx, key in enumerate(xml_data.keys()):
        xml_data[key] = get_xml(urls[idx])

    #   reconstruct xml structure
    for idx, cat in enumerate(xml_data.keys()):
        limit = 9 if cat == "highlights" else 3
        items = xml_data[cat].find_all("item", limit=limit)
        xml_data[cat] = xml_funcs[idx](items)

    print(xml_data)


    # write new structure to file
    for cat in xml_data.keys():
        ext = str(os.getenv("OUTPUT_FILE_EXT"))
        path = str(os.getenv("PWD")) + "/" + str(os.getenv("OUTPUT_FOLDER"))
        write_xml_file(cat,ext, path,xml_data[cat])

if __name__ == '__main__':
    try:
        main()
    except EnvNotFound:
        print()
    except (EnvNotFound, UrlNotFound) as e:
        print(e.e_message)

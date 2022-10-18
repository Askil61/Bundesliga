from bs4 import BeautifulSoup
from yattag.doc import Doc
from yattag.indentation import indent


def get_highlights(items:list) -> list:
    doc, tag, text, _ = Doc().ttl()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

    with tag("n24news"):
        for item in items:
            with tag("news"):
                with tag("topic"):
                    text(item.find("title").string)
                with tag("published", type="timestamp"):
                    text(item.find("pubDate").string)
                with tag("guid"):
                    text(item.find('guid').string)
                with tag("video"):
                    text(item.find("media:content", type="video/mp4").get("url"))
    result = indent(
        doc.getvalue(),
        indentation="    ",
        newline="\n",
        # indent_text = True
    )
    return result

def get_news(items:list) -> list:
    doc, tag, text, _ = Doc().ttl()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

    with tag("n24news"):
        for item in items:
            with tag("news"):
                with tag("guid"):
                    text(item.find("guid").string)
                with tag("headline"):
                    text(item.find("title").string)
                with tag("subline"):
                    text(item.find("welt:topic").string)
                with tag("textmessage"):
                    text(item.find('description').string)
                with tag("image", type="remotefile"):
                    text(item.find("media:content", type="image/jpeg").get("url"))
                with tag("published", type="timestamp"):
                    text(item.find("pubDate").string)
                with tag("source"):
                    text(item.find("dc:source").string)
    result = indent(
        doc.getvalue(),
        indentation="    ",
        newline="\n",
        # indent_text = True
    )
    return result


if __name__ == '__main__':
    get_highlights()

import re
import requests
from bs4 import BeautifulSoup


def get(sticker_id, index):
    res = requests.get(f"https://store.line.me/stickershop/product/{sticker_id}")
    soup = BeautifulSoup(res.content, "html.parser")
    try:
        elem = soup.select(".FnImage span")[index]
        img_url = re.search(r'\((.+)\)', elem.get("style")).group(1)
        imgres = requests.get(img_url)
        return imgres.content
    except Exception:
        return False

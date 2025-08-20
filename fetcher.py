import requests
from bs4 import BeautifulSoup
from config import HEADERS, COOKIES, PROXIES
from parser import parse_posts_to_json

session = requests.Session()
session.headers.update(HEADERS)
session.cookies.update(COOKIES)
session.proxies.update(PROXIES)

def fetch_posts(url: str, debug=False):
    try:
        r = session.get(url, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[ERROR] 请求失败: {url} - {e}")
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    posts = []

    post_elements = soup.select("div.atl-item.post")
    if debug:
        print(f"[DEBUG] {url} 抓取到 {len(post_elements)} 条帖子")

    for idx, post in enumerate(post_elements, start=1):
        author_tag = post.select_one("div.atl-head .atl-info span a.js-vip-check")
        author = author_tag.get_text(strip=True) if author_tag else "未知作者"

        time_tag = post.select_one("div.atl-head .atl-info span span.time")
        timestamp = time_tag.get_text(strip=True) if time_tag else "未知时间"

        content_div = post.select_one("div.atl-content div.atl-con-bd div.bbs-content")
        content = content_div.get_text("\n", strip=True) if content_div else "无内容"

        posts.append((author, timestamp, content))

    return parse_posts_to_json(posts)

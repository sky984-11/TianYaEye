import time
import json
from datetime import datetime
from fetcher import fetch_posts
from notifier import send_feishu
from config import URLS, INTERVAL

def monitor(debug=False):
    last_floors = {url: None for url in URLS}  # 记录每个URL的最后一条楼层

    round_num = 0
    while True:
        round_num += 1
        print(f"\n[INFO] 第 {round_num} 次轮询 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        for url in URLS:
            try:
                posts = fetch_posts(url, debug=debug)
                if not posts:
                    continue

                latest_post = posts[-1]
                latest_floor = latest_post["floor"]

                if latest_floor != last_floors[url]:
                    last_floors[url] = latest_floor
                    send_feishu(f"[{url}] {latest_post['content']}")
                    print(json.dumps(latest_post, ensure_ascii=False, indent=2))
                else:
                    if debug:
                        print(f"[DEBUG] {url} 最后一条楼层未变化")

            except Exception as e:
                print(f"[ERROR] {url} 处理失败: {e}")

        time.sleep(INTERVAL)

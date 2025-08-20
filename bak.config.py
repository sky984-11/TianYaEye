# 全局配置

# 需要监听的帖子链接，可以放多个
URLS = [
    "https://tianya.at/thread/0/*****",
]

FEISHU_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxx"

HEADERS = {
    "user-agent": "Mozilla/5.0 ..."
}

COOKIES = {
    "uuid": "xxx",
    "uid": "xxx",
    "key": "xxx",
    "token": "xxx",
}

PROXIES = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890"
}

INTERVAL = 240  # 每轮轮询间隔

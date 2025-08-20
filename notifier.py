import requests
from config import FEISHU_WEBHOOK

def send_feishu(text: str):
    payload = {"msg_type": "text", "content": {"text": text}}
    try:
        r = requests.post(FEISHU_WEBHOOK, json=payload, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print("[ERROR] 飞书通知失败:", e)

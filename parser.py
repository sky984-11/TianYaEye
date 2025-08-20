import re

def parse_posts_to_json(posts):
    result = []
    for author, timestamp, content in posts:
        floor = timestamp
        uid = author

        reply_to = None
        reply_floor = None

        reply_to_match = re.search(r'@[\w\u4e00-\u9fa5]+', content)
        if reply_to_match:
            reply_to = reply_to_match.group()

        reply_floor_match = re.search(r'#\d+楼', content)
        if reply_floor_match:
            reply_floor = reply_floor_match.group()

        clean_content = re.sub(r'@[\w\u4e00-\u9fa5]+', '', content)
        clean_content = re.sub(r'#\d+楼', '', clean_content).strip()

        result.append({
            "floor": floor,
            "uid": uid,
            "content": clean_content,
            "reply_to": reply_to,
            "reply_floor": reply_floor
        })
    return result

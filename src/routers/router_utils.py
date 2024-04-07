from datetime import datetime

def format_response(content, timestamp: datetime = None):
    if timestamp is None:
        timestamp = datetime.now()
    return {
        "timestamp": timestamp.isoformat(),
        "content": content
    }
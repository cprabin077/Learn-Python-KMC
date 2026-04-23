from  datetime import datetime

def log_event(even_type, *args, **kwargs):
    if not isinstance(even_type, str):
        return {
            "error": "Event type must be string"
        }
    
    if len(args) <= 0:
        return {
            "error": "Provide at least one message"
        }

    if kwargs.get('priority') == "high":
        kwargs['alert'] = True
        
    return {
        "type": even_type,
        "messages": list(args),
        "meta": kwargs
    }

print(log_event(1)) # Message is not provided
print(log_event("ERROR", "error", user = "Admin"))
# {'type': 'ERROR', 'messages': ['error'], 'meta': {'user': 'Admin'}}
print(log_event("ERROR", "error", user = "User", timestamp = f'{datetime.now()}', priority = "low"))
# {'type': 'ERROR', 'messages': ['error'], 'meta': {'user': 'User', 'timestamp': '2026-04-23 15:01:26.510646', 'priority': 'low'}}
print(log_event("ERROR", "error", user = "Admin", timestamp = "2026-4-23", priority = "high"))
# {'type': 'ERROR', 'messages': ['error'], 'meta': {'user': 'Admin', 'timestamp': 1999, 'priority': 'high', 'alert': True}}
print(log_event("ERROR", "error", user = "User", timestamp = f'{datetime.now()}', priority = "high"))
# {'type': 'ERROR', 'messages': ['error'], 'meta': {'user': 'User', 'timestamp': '2026-04-23 15:01:03.297427', 'priority': 'high', 'alert': True}}

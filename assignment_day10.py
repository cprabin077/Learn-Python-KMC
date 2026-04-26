from datetime import datetime
# event log
def log_event(event_type, *args, **kwargs):

    # Check if messages are provided
    if len(args) == 0:
        return "No messages provided"

    # Convert messages into list
    messages = list(args)

    # Copy kwargs into meta
    meta = dict(kwargs)

    # Add timestamp (only if not already given)
    if "timestamp" not in meta:
        meta["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check priority
    if "priority" in meta and meta["priority"].lower() == "high":
        meta["alert"] = True

    # Create final dictionary
    result = {
        "type": event_type,
        "messages": messages,
        "meta": meta
    }

    return result

# print(log_event()) # TypeError: log_event() missing 1 required positional argument: 'event_type'
print(log_event(1)) 
# No messages provided
print(log_event("INFO", "System started"))
# {'type': 'INFO', 'messages': ['System started'], 'meta': {}}
print(log_event("DEBUG", "Step 1", "Step 2", user="admin")) 
# {'type': 'DEBUG', 'messages': ['Step 1', 'Step 2'], 'meta': {'user': 'admin'}}
print(log_event("ERROR", "Crash detected", priority="HIGH", timestamp = "2026-01-01 12:00:00"))
# {'type': 'ERROR', 'messages': ['Crash detected'], 'meta': {'priority': 'HIGH', 'alert': True}} 

#  Another method
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



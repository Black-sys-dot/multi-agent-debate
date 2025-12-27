import json, time
from datetime import datetime

def log_event(event):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"project/logs/debate_log_{timestamp}.json", "a") as f:
        f.write(json.dumps({
            "timestamp": time.time(),
            "event": event
        },indent=2) + "\n")

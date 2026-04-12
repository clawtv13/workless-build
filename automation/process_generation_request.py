#!/usr/bin/env python3
"""Helper for OpenClaw agent to process generation requests"""

import json
from pathlib import Path

QUEUE_DIR = Path('/tmp/workless-generation')
REQUEST_FILE = QUEUE_DIR / 'request.json'
RESPONSE_FILE = QUEUE_DIR / 'response.md'
LOCK_FILE = QUEUE_DIR / 'lock'

def get_pending_request():
    """Check if there's a pending generation request"""
    
    if not REQUEST_FILE.exists() or not LOCK_FILE.exists():
        return None
    
    try:
        data = json.loads(REQUEST_FILE.read_text(encoding='utf-8'))
        return data
    except:
        return None

def save_response(content):
    """Save generated article and remove lock"""
    
    RESPONSE_FILE.write_text(content, encoding='utf-8')
    
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()
    
    print(f"✓ Response saved: {len(content)} chars")

if __name__ == "__main__":
    request = get_pending_request()
    
    if request:
        print(f"📋 Pending request:")
        print(f"  Title: {request['title']}")
        print(f"  Source: {request['source']}")
    else:
        print("No pending requests")

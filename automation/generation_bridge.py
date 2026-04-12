#!/usr/bin/env python3
"""Bridge between automation and OpenClaw agent for article generation"""

import json
import time
from pathlib import Path
from datetime import datetime

QUEUE_DIR = Path('/tmp/workless-generation')
REQUEST_FILE = QUEUE_DIR / 'request.json'
RESPONSE_FILE = QUEUE_DIR / 'response.md'
LOCK_FILE = QUEUE_DIR / 'lock'

def ensure_queue_dir():
    """Create queue directory if needed"""
    QUEUE_DIR.mkdir(exist_ok=True, mode=0o755)

def request_generation(item):
    """Request article generation from OpenClaw agent"""
    
    ensure_queue_dir()
    
    # Check if previous request is still pending
    if REQUEST_FILE.exists() and LOCK_FILE.exists():
        age = time.time() - REQUEST_FILE.stat().st_mtime
        if age < 300:  # 5 min timeout
            print(f"  ⏳ Previous request pending ({int(age)}s old). Waiting...")
            return None
    
    # Clear old files
    for f in [REQUEST_FILE, RESPONSE_FILE, LOCK_FILE]:
        if f.exists():
            f.unlink()
    
    # Write request
    request = {
        'title': item['title'],
        'summary': item['summary'],
        'source': item['source'],
        'url': item.get('url', ''),
        'timestamp': datetime.now().isoformat(),
    }
    
    REQUEST_FILE.write_text(json.dumps(request, indent=2), encoding='utf-8')
    LOCK_FILE.touch()
    
    print(f"  📝 Generation request created: {REQUEST_FILE}")
    print(f"  ⏳ Waiting for OpenClaw agent (max 180s)...")
    
    # Wait for response (up to 3 min)
    start = time.time()
    while time.time() - start < 180:
        if RESPONSE_FILE.exists() and not LOCK_FILE.exists():
            # Response ready
            content = RESPONSE_FILE.read_text(encoding='utf-8')
            
            # Cleanup
            REQUEST_FILE.unlink()
            RESPONSE_FILE.unlink()
            
            print(f"  ✓ Article generated ({len(content)} chars)")
            return content
        
        time.sleep(2)
    
    # Timeout
    print(f"  ✗ Timeout waiting for generation")
    
    # Cleanup
    for f in [REQUEST_FILE, LOCK_FILE]:
        if f.exists():
            f.unlink()
    
    return None

if __name__ == "__main__":
    # Test
    test_item = {
        'title': 'Test Article Generation',
        'summary': 'This is a test summary for article generation',
        'source': 'Test Source',
        'url': 'https://test.com'
    }
    
    content = request_generation(test_item)
    if content:
        print("SUCCESS!")
        print(content[:200])
    else:
        print("FAILED")

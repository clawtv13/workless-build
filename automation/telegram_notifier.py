#!/usr/bin/env python3
"""Send Telegram notifications when posts published"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '8116230130')

def send_notification(title, url, category='News'):
    """Send Telegram message"""
    
    if not TELEGRAM_BOT_TOKEN:
        print("⚠️  TELEGRAM_BOT_TOKEN not set. Skipping notification.")
        return False
    
    message = f"✅ Published: {title}\n\n📂 Category: {category}\n🔗 {url}"
    
    try:
        response = requests.post(
            f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
            json={
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message,
                'parse_mode': 'HTML',
                'disable_web_page_preview': False
            },
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"  ✓ Telegram notification sent")
            return True
        else:
            print(f"  ✗ Telegram failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ✗ Telegram error: {e}")
        return False

if __name__ == "__main__":
    # Test
    send_notification(
        "Test Post Title",
        "https://workless.build/news/test",
        "News"
    )

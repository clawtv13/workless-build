#!/usr/bin/env python3
"""Master cron job orchestrator - runs at 08:00, 12:00, 16:00, 20:00 UTC"""

import sys
import sqlite3
from pathlib import Path
from datetime import datetime
import subprocess

sys.path.insert(0, str(Path(__file__).parent))

from database import DB_PATH, get_unprocessed, mark_processed, mark_published
from quality_reviewer import review_article
from publisher import build_site, deploy_to_github
from telegram_notifier import send_notification

# Category mix: 50% news, 25% tutorials, 25% reviews/casos
CATEGORY_MIX = {
    8: 'news',      # Morning: news
    12: 'tutorial',  # Noon: tutorial
    16: 'review',    # Afternoon: review/tool
    20: 'news'       # Evening: news
}

def get_posts_published_today():
    """Count posts published today"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Check if published_at column exists
    try:
        c.execute(f"SELECT COUNT(*) FROM content_queue WHERE published = 1 AND date(discovered_at) = '{today}'")
        count = c.fetchone()[0]
    except:
        count = 0
    
    conn.close()
    return count

def get_best_item_for_category(category, limit=5):
    """Get highest scored unprocessed item for category"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Map category to type
    if category in ['news']:
        type_filter = 'news'
    elif category == 'tutorial':
        type_filter = 'tutorial'
    else:  # review or casos-de-uso
        type_filter = 'review'  # TODO: expand when we have caso-de-uso in DB
    
    c.execute('''
        SELECT * FROM content_queue 
        WHERE processed = 0 AND type = ?
        ORDER BY score DESC, discovered_at DESC
        LIMIT ?
    ''', (type_filter, limit))
    
    items = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return items[0] if items else None

def generate_article_via_openclaw(item):
    """Generate article using OpenClaw (simulated here)"""
    # In production, this would call OpenClaw or spawn subagent
    # For now, placeholder that would be replaced with real generation
    
    print(f"  📝 Generating article for: {item['title'][:50]}...")
    
    # Placeholder - in real system, this calls your generation logic
    # For now, returning simple structure
    article_content = f"""---
title: "{item['title']}"
description: "{item['summary'][:150]}"
date: {datetime.now().strftime('%Y-%m-%d')}
author: "WorkLess AI Team"
category: "{item['source'].lower().replace(' ', '')}"
tags: ["ia", "{item['type']}"]
source: "{item['source']}"
sourceUrl: "{item['url']}"
featured: false
---

# {item['title']}

{item['summary']}

[Content would be generated here by OpenClaw/AI]
"""
    
    return article_content

def run_scheduled_post():
    """Run one post cycle"""
    
    hour = datetime.now().hour
    current_time = datetime.now().strftime('%H:%M UTC')
    
    print(f"🤖 WorkLess Automation - {current_time}")
    print("=" * 60)
    
    # Determine category for this time slot
    category = CATEGORY_MIX.get(hour, 'news')
    print(f"📂 Category: {category}")
    
    # Check daily quota
    published_today = get_posts_published_today()
    print(f"📊 Posts today: {published_today}")
    
    if published_today >= 5:
        print("✓ Daily quota reached (5 posts). Skipping.")
        return
    
    # Get best item
    item = get_best_item_for_category(category)
    
    if not item:
        print(f"⚠️  No unprocessed {category} items. Skipping.")
        return
    
    print(f"🎯 Selected: {item['title'][:60]}... (score: {item.get('score', 0)}/50)")
    
    # Generate article
    draft = generate_article_via_openclaw(item)
    
    # Quality review
    print(f"✨ Quality review...")
    review_result = review_article(draft)
    
    quality_score = review_result['quality_score']
    print(f"  Quality: {quality_score}/10")
    
    if quality_score < 6:
        print(f"  ✗ Quality too low ({quality_score}/10). Skipping.")
        mark_processed(item['id'])
        return
    
    if quality_score < 8:
        print(f"  ⚠️  Quality moderate ({quality_score}/10). Would notify user.")
        # In production: send notification for manual review
        # For now: skip
        return
    
    # Save article
    slug = item['title'].lower().replace(' ', '-')[:60]
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    
    article_path = REPO_PATH / 'src' / 'content' / 'news' / f"{slug}.md"
    article_path.write_text(review_result['content'], encoding='utf-8')
    print(f"  ✓ Saved: {article_path.name}")
    
    # Build + Deploy
    if build_site() and deploy_to_github():
        # Notify
        url = f"https://workless.build/news/{slug}"
        send_notification(item['title'], url, category.title())
        
        # Mark published
        mark_published(item['id'])
        mark_processed(item['id'])
        
        print(f"\n✅ POST PUBLISHED!")
    else:
        print(f"\n✗ Deploy failed")

REPO_PATH = Path(__file__).parent.parent

if __name__ == "__main__":
    run_scheduled_post()

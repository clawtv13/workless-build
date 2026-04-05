#!/usr/bin/env python3
"""RSS feed scraper for AI news sources"""

import feedparser
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from database import add_to_queue

RSS_FEEDS = {
    'OpenAI': 'https://openai.com/blog/rss',
    'Anthropic': 'https://www.anthropic.com/news/rss',
    'Google AI': 'https://blog.google/technology/ai/rss/',
    'DeepMind': 'https://deepmind.google/blog/rss/',
    'HuggingFace': 'https://huggingface.co/blog/feed.xml',
    'Stability AI': 'https://stability.ai/blog/rss',
}

def scrape_rss_feeds():
    """Scrape all RSS feeds and add to queue"""
    total_added = 0
    total_duplicates = 0
    
    for source_name, feed_url in RSS_FEEDS.items():
        print(f"📡 Scraping {source_name}...")
        
        try:
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:10]:  # Latest 10 per feed
                title = entry.get('title', 'No title')
                url = entry.get('link', '')
                summary = entry.get('summary', entry.get('description', ''))
                
                # Clean HTML from summary
                from bs4 import BeautifulSoup
                summary_clean = BeautifulSoup(summary, 'html.parser').get_text()[:500]
                
                result = add_to_queue(
                    source=source_name,
                    content_type='news',
                    title=title,
                    url=url,
                    summary=summary_clean,
                    raw_content="",
                    metadata=""
                )
                
                if result:
                    total_added += 1
                    print(f"  ✓ Added: {title[:60]}...")
                else:
                    total_duplicates += 1
                    print(f"  ⊘ Duplicate: {title[:60]}...")
        
        except Exception as e:
            print(f"  ✗ Error scraping {source_name}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"  New items: {total_added}")
    print(f"  Duplicates: {total_duplicates}")
    
    return total_added

if __name__ == "__main__":
    scrape_rss_feeds()

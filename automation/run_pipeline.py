#!/usr/bin/env python3
"""Master pipeline orchestrator"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from database import init_database
from sources.rss_scraper import scrape_rss_feeds
from content_generator import process_queue

def run_full_pipeline():
    """Run complete pipeline: scrape → generate → publish"""
    
    print("🚀 WorkLess AI - Full Pipeline\n")
    print("=" * 60)
    
    # Step 1: Initialize database
    print("\n📦 Step 1: Database")
    init_database()
    
    # Step 2: Scrape sources
    print("\n📡 Step 2: Scraping Sources")
    new_items = scrape_rss_feeds()
    
    if new_items == 0:
        print("\n✓ No new content found. Pipeline complete.")
        return
    
    # Step 3: Generate content
    print("\n✍️  Step 3: Generating Content")
    process_queue(limit=5)  # Process 5 at a time
    
    # Step 4: Build site
    print("\n🏗️  Step 4: Building Site")
    import subprocess
    result = subprocess.run(
        ['npm', 'run', 'build'],
        cwd=Path(__file__).parent.parent,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("  ✓ Site built successfully")
    else:
        print(f"  ✗ Build failed: {result.stderr[:200]}")
    
    print("\n" + "=" * 60)
    print("✅ Pipeline complete!")

if __name__ == "__main__":
    run_full_pipeline()

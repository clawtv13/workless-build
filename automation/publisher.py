#!/usr/bin/env python3
"""Build site and deploy to GitHub Pages"""

import subprocess
import os
from pathlib import Path
from dotenv import load_dotenv
from telegram_notifier import send_notification

load_dotenv()

REPO_PATH = Path(__file__).parent.parent
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO = os.getenv('GITHUB_REPO', 'clawtv13/workless-build')

def build_site():
    """Run npm build"""
    print("🏗️  Building site...")
    
    result = subprocess.run(
        ['npm', 'run', 'build'],
        cwd=REPO_PATH,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("  ✓ Build successful")
        return True
    else:
        print(f"  ✗ Build failed: {result.stderr[:200]}")
        return False

def deploy_to_github():
    """Deploy dist/ to gh-pages branch"""
    print("🚀 Deploying to GitHub Pages...")
    
    dist_path = REPO_PATH / 'dist'
    
    # Prepare git
    commands = [
        f"cd {dist_path} && rm -rf .git",
        f"cd {dist_path} && git init",
        f"cd {dist_path} && git config user.email 'deploy@workless.build'",
        f"cd {dist_path} && git config user.name 'WorkLess Deploy'",
        f"cd {dist_path} && echo 'workless.build' > CNAME",
        f"cd {dist_path} && touch .nojekyll",
        f"cd {dist_path} && git add -A",
        f"cd {dist_path} && git commit -m 'Deploy: {os.popen('date +\"%Y-%m-%d %H:%M\"').read().strip()}'",
        f"cd {dist_path} && git push -f https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git master:gh-pages"
    ]
    
    for cmd in commands:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0 and 'nothing to commit' not in result.stdout:
            print(f"  ✗ Command failed: {cmd[:50]}...")
            return False
    
    print("  ✓ Deployed successfully")
    return True

def publish_post(article_title, article_slug, category='News'):
    """Full publish pipeline"""
    
    print(f"\n📤 Publishing: {article_title[:50]}...\n")
    
    # Build
    if not build_site():
        return False
    
    # Deploy
    if not deploy_to_github():
        return False
    
    # Notify
    url = f"https://workless.build/news/{article_slug}"
    send_notification(article_title, url, category)
    
    print(f"\n✅ Published successfully!")
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        publish_post(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'News')
    else:
        print("Usage: python publisher.py 'Article Title' 'article-slug' 'Category'")

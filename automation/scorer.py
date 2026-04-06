#!/usr/bin/env python3
"""Score content items for publication priority"""

import sys
from pathlib import Path
import sqlite3
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent))

DB_PATH = Path(__file__).parent / "content.db"

# Keywords para scoring
IMPACT_KEYWORDS = ['lanzamiento', 'gratis', 'nuevo modelo', 'breakthrough', 'disponible', 'acceso']
ACTIONABLE_KEYWORDS = ['cómo', 'tutorial', 'guía', 'paso a paso', 'herramienta', 'usar']
TRENDING_SOURCES = ['OpenAI', 'Anthropic', 'Google AI', 'DeepMind']

def score_impact(item):
    """Score 0-10: Qué tan importante es"""
    score = 5  # Base
    
    title_lower = item['title'].lower()
    
    # High impact keywords
    if any(kw in title_lower for kw in ['gpt-5', 'gemini 3', 'claude 4', 'llama 4']):
        score += 5
    elif any(kw in title_lower for kw in IMPACT_KEYWORDS):
        score += 2
    
    # Source authority
    if item['source'] in TRENDING_SOURCES:
        score += 1
    
    return min(score, 10)

def score_relevance(item):
    """Score 0-10: Relevancia para audiencia española"""
    score = 6  # Base (most AI news is globally relevant)
    
    title_lower = item['title'].lower()
    
    # Global tools everyone uses
    if any(kw in title_lower for kw in ['chatgpt', 'gemini', 'claude', 'midjourney', 'openai']):
        score += 3
    
    # Developer/technical audiences (Spain has strong dev community)
    if any(kw in title_lower for kw in ['api', 'developer', 'code', 'open source']):
        score += 1
    
    # Free/accessible
    if 'free' in title_lower or 'gratis' in title_lower or 'open source' in title_lower:
        score += 2
    
    return min(score, 10)

def score_actionability(item):
    """Score 0-10: Usuario puede usar esto hoy"""
    score = 4  # Base
    
    title_lower = item['title'].lower()
    
    # Direct actionable keywords
    if any(kw in title_lower for kw in ACTIONABLE_KEYWORDS):
        score += 4
    
    # Available now vs "coming soon"
    if any(kw in title_lower for kw in ['available', 'launch', 'release', 'now']):
        score += 2
    elif any(kw in title_lower for kw in ['soon', 'preview', 'beta waitlist']):
        score -= 2
    
    # Type of content
    if item['type'] == 'tutorial':
        score += 2
    
    return max(min(score, 10), 0)

def score_timeliness(item):
    """Score 0-10: Qué tan fresco es"""
    try:
        discovered = datetime.fromisoformat(item['discovered_at'].replace('Z', '+00:00'))
        age_hours = (datetime.now() - discovered).total_seconds() / 3600
        
        if age_hours < 6:
            return 10
        elif age_hours < 24:
            return 8
        elif age_hours < 72:
            return 6
        elif age_hours < 168:  # 1 week
            return 4
        else:
            return 2
    except:
        return 5  # Default if can't parse

def score_differentiation(item):
    """Score 0-10: Qué tan único/diferenciado es"""
    score = 5  # Base
    
    title_lower = item['title'].lower()
    
    # Technical depth (less covered in Spanish)
    if any(kw in title_lower for kw in ['architecture', 'benchmark', 'research', 'paper']):
        score += 2
    
    # Practical tutorials (valuable)
    if item['type'] in ['tutorial', 'review']:
        score += 2
    
    # Major announcements (everyone covers but still important)
    if any(kw in title_lower for kw in ['gpt-5', 'gemini 3', 'major']):
        score -= 1  # Everyone will cover
    
    return min(score, 10)

def score_item(item):
    """Calculate total score for item (0-50)"""
    impact = score_impact(item)
    relevance = score_relevance(item)
    actionability = score_actionability(item)
    timeliness = score_timeliness(item)
    differentiation = score_differentiation(item)
    
    total = impact + relevance + actionability + timeliness + differentiation
    
    return {
        'total': total,
        'impact': impact,
        'relevance': relevance,
        'actionability': actionability,
        'timeliness': timeliness,
        'differentiation': differentiation
    }

def update_scores():
    """Score all unscored items in database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Add score column if doesn't exist
    try:
        c.execute('ALTER TABLE content_queue ADD COLUMN score INTEGER DEFAULT 0')
        c.execute('ALTER TABLE content_queue ADD COLUMN score_breakdown TEXT')
        conn.commit()
    except sqlite3.OperationalError:
        pass  # Column already exists
    
    # Get unscored items
    c.execute('SELECT * FROM content_queue WHERE score = 0 OR score IS NULL')
    items = [dict(row) for row in c.fetchall()]
    
    print(f"📊 Scoring {len(items)} items...\n")
    
    for item in items:
        scores = score_item(item)
        
        c.execute('''
            UPDATE content_queue 
            SET score = ?, score_breakdown = ?
            WHERE id = ?
        ''', (scores['total'], str(scores), item['id']))
        
        print(f"  {item['id']:3d}. {scores['total']:2d}/50 - {item['title'][:50]}...")
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Scored {len(items)} items")

if __name__ == "__main__":
    update_scores()

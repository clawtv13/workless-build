#!/usr/bin/env python3
"""Generate content from queue using AI + quality pipeline"""

import os
import sys
from pathlib import Path
from datetime import datetime
from openai import OpenAI

sys.path.insert(0, str(Path(__file__).parent))
from database import get_unprocessed, mark_processed

# Will be set via .env
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY', 'placeholder'))

def generate_news_article(item):
    """Generate Spanish news article from English source"""
    
    prompt = f"""Eres un periodista tech especializado en IA. 

Título original: {item['title']}
Resumen: {item['summary']}
Fuente: {item['source']}

Tarea: Escribe un artículo en español (400-600 palabras) sobre esta noticia.

Estructura:
1. Lead paragraph (qué pasó, por qué importa)
2. Contexto/background
3. Detalles técnicos (accesibles)
4. Implicaciones/impacto
5. Qué significa para usuarios

Tono: Profesional pero accesible. No hype, facts.
Audiencia: Mix de técnicos y no-técnicos.

NO uses frases como "en conclusión", "en resumen", "cabe destacar".
Escribe directo, claro, valioso.

Artículo:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500
        )
        
        content = response.choices[0].message.content
        return content
        
    except Exception as e:
        print(f"✗ Error generating content: {e}")
        return None

def save_to_content_collection(item, generated_content):
    """Save generated content as markdown in Astro content collection"""
    
    # Create slug from title
    import re
    slug = re.sub(r'[^\w\s-]', '', item['title'].lower())
    slug = re.sub(r'[-\s]+', '-', slug)[:60]
    
    # Format date
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Build frontmatter
    frontmatter = f"""---
title: "{item['title']}"
description: "{item['summary'][:150]}"
date: {date_str}
author: "WorkLess AI Team"
category: "{item['source'].lower().replace(' ', '')}"
tags: ["ia", "noticias", "{item['source'].lower()}"]
source: "{item['source']}"
sourceUrl: "{item['url']}"
featured: false
---

"""
    
    full_content = frontmatter + generated_content
    
    # Save to content/news/
    content_dir = Path(__file__).parent.parent / "src" / "content" / "news"
    content_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(full_content, encoding='utf-8')
    
    print(f"  ✓ Saved: {filepath.name}")
    return str(filepath)

def process_queue(limit=5):
    """Process items from queue"""
    
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  OPENAI_API_KEY not set. Skipping generation.")
        print("   Set it in .env file to enable content generation.")
        return
    
    items = get_unprocessed(limit=limit)
    
    if not items:
        print("📭 No unprocessed items in queue")
        return
    
    print(f"📝 Processing {len(items)} items...\n")
    
    for item in items:
        print(f"🔄 Generating: {item['title'][:60]}...")
        
        if item['type'] == 'news':
            content = generate_news_article(item)
            
            if content:
                save_to_content_collection(item, content)
                mark_processed(item['id'])
                print(f"  ✅ Complete\n")
            else:
                print(f"  ✗ Failed\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=5, help='Number of items to process')
    args = parser.parse_args()
    
    process_queue(limit=args.limit)

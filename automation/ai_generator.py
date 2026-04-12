#!/usr/bin/env python3
"""
Fixed AI article generator - generates REAL content, not templates
"""
import re, os
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_article_real(item):
    """Generate actual article content using GPT-4"""
    
    print(f"  📝 Generating real content for: {item['title'][:50]}...")
    
    prompt = f"""Write a 400-500 word news article in Spanish about:

Title: {item['title']}
Summary: {item['summary']}
Source: {item['source']}

Requirements:
- Write UNIQUE content, not a template
- Be specific about what changed/was announced
- Explain why it matters in practical terms
- Use natural Spanish, avoid AI phrases like "marca un avance significativo", "ecosistema", "robusto"
- Structure: Brief intro → What changed → Why it matters → Practical impact
- No generic bullets - be specific to THIS topic
- Conversational tone, like explaining to a colleague
- No fluff, get to the point

Format as markdown with ## headings."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un periodista tech que escribe artículos claros y específicos. Evitas frases genéricas de AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        content = response.choices[0].message.content.strip()
        
        # Validate minimum length
        if len(content) < 300:
            print(f"  ⚠️  Content too short ({len(content)} chars), regenerating...")
            return generate_article_real(item)  # Retry once
        
        print(f"  ✓ Generated {len(content)} chars")
        return content
        
    except Exception as e:
        print(f"  ✗ Generation failed: {e}")
        return None

def build_full_article(item, content, image_path=None):
    """Build complete article with frontmatter"""
    
    slug = re.sub(r'[^\w\s-]', '', item['title'].lower())
    slug = re.sub(r'[-\s]+', '-', slug)[:60]
    
    # Map source to category
    source = item.get('source', 'otros').lower()
    category_map = {
        'google': 'google',
        'openai': 'openai',
        'anthropic': 'anthropic',
        'meta': 'meta',
        'huggingface': 'investigacion',
        'research': 'investigacion',
    }
    
    category = 'otros'
    for key, val in category_map.items():
        if key in source:
            category = val
            break
    
    image_field = f'\nimage: "{image_path}"' if image_path else ''
    
    article = f"""---
title: "{item['title']}"
description: "{item['summary'][:150]}"
date: {datetime.now().strftime('%Y-%m-%d')}
author: "WorkLess AI Team"
category: "{category}"
tags: ["ia", "noticias"]
source: "{item.get('source', 'Unknown')}"
sourceUrl: "{item.get('url', '')}"
featured: false{image_field}
---

{content}
"""
    
    return article, slug

if __name__ == "__main__":
    # Test with real item
    test_item = {
        'title': 'Google lanza Gemini 2.0 Flash con audio en tiempo real',
        'summary': 'Nueva versión de Gemini con capacidades de audio streaming',
        'source': 'Google AI',
        'url': 'https://blog.google/technology/ai/google-gemini-2/'
    }
    
    content = generate_article_real(test_item)
    if content:
        article, slug = build_full_article(test_item, content)
        print("\n" + "="*50)
        print(article[:500])

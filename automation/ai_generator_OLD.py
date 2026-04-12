#!/usr/bin/env python3
"""AI generation wrapper that uses OpenClaw's context"""

import re
from datetime import datetime
from generation_bridge import request_generation

def generate_article(item):
    """Generate article via OpenClaw agent (file-based bridge)"""
    
    print(f"  📝 Requesting article generation...")
    
    try:
        content = request_generation(item)
        
        if content:
            return content
        else:
            print(f"  ⚠️  Bridge timeout. Using fallback mock.")
            # Fallback to basic mock if agent doesn't respond
            return generate_mock_article(item)
            
    except Exception as e:
        print(f"  ✗ Generation error: {e}")
        return generate_mock_article(item)

def generate_mock_article(item):
    """Fallback mock article if bridge fails"""
    
    title_short = item['title'].split(':')[0] if ':' in item['title'] else item['title']
    
    content = f"""**{title_short}** marca un avance significativo en el ecosistema de IA, según anunció {item['source']}.

## Qué cambia

{item['summary'][:200]}

Esta actualización permite:
- Mayor flexibilidad en implementación
- Mejor control de costos
- Optimización de rendimiento

## Impacto

La comunidad de desarrolladores recibirá acceso a capacidades mejoradas que facilitan la construcción de aplicaciones de IA más robustas.

## Disponibilidad

Ya disponible en la plataforma de {item['source']}.

*Nota: Este artículo fue generado automáticamente. Para más detalles, consulta la [fuente original]({item.get('url', '#')}).*
"""
    
    return content

def build_full_article(item, content, image_path=None):
    """Build complete article with frontmatter"""
    
    slug = re.sub(r'[^\w\s-]', '', item['title'].lower())
    slug = re.sub(r'[-\s]+', '-', slug)[:60]
    
    # Map source to valid category
    source = item.get('source', 'otros').lower()
    category_map = {
        'google': 'google',
        'google ai': 'google',
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
    
    # Add image field if generated
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
    # Test
    test_item = {
        'title': 'Test Article',
        'summary': 'This is a test summary',
        'source': 'Test Source',
        'url': 'https://test.com'
    }
    
    content = generate_article(test_item)
    if content:
        article, slug = build_full_article(test_item, content)
        print(f"Generated: {slug}")
        print(article[:200])

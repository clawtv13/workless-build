#!/usr/bin/env python3
"""Quality review for generated articles"""

import re

# AI patterns to remove/fix
AI_PATTERNS = [
    r'[Ee]n conclusión',
    r'[Cc]abe destacar',
    r'[Ee]s importante señalar',
    r'[Ee]n resumen',
    r'[Ss]in duda',
    r'[Dd]efinitivamente',
    r'[Cc]laramente',
    r'[Ee]videntemente'
]

def remove_ai_patterns(text):
    """Remove common AI tells"""
    for pattern in AI_PATTERNS:
        text = re.sub(pattern + r'\s*,?\s*', '', text)
    return text

def check_structure(text):
    """Verify article has proper structure"""
    issues = []
    
    # Check for headers
    if not re.search(r'^##\s+', text, re.MULTILINE):
        issues.append("No headers found (needs ## sections)")
    
    # Check paragraph length (not walls of text)
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    long_paragraphs = [p for p in paragraphs if len(p) > 1000]
    if long_paragraphs:
        issues.append(f"{len(long_paragraphs)} paragraphs too long (>1000 chars)")
    
    # Check for lists (good for scannability)
    has_lists = bool(re.search(r'^\s*[-*]\s+', text, re.MULTILINE))
    
    return issues, has_lists

def humanize_text(text):
    """Make text more natural"""
    # Remove AI patterns
    text = remove_ai_patterns(text)
    
    # Fix overly formal phrases
    text = text.replace('a continuación', 'ahora')
    text = text.replace('cabe mencionar', '')
    text = text.replace('es fundamental', 'necesitas')
    text = text.replace('es esencial', 'importa')
    
    # Remove redundant transitions
    text = re.sub(r'\n\n(Además|Asimismo|Por otro lado),\s*', '\n\n', text)
    
    return text

def score_quality(text):
    """Score article quality 0-10"""
    score = 7  # Base (assume decent)
    
    # Structure check
    issues, has_lists = check_structure(text)
    if issues:
        score -= len(issues)
    if has_lists:
        score += 1
    
    # Length check (400-800 words = sweet spot)
    word_count = len(text.split())
    if 400 <= word_count <= 800:
        score += 1
    elif word_count < 300:
        score -= 2
    elif word_count > 1200:
        score -= 1
    
    # AI pattern check
    ai_pattern_count = sum(1 for pattern in AI_PATTERNS if re.search(pattern, text, re.IGNORECASE))
    if ai_pattern_count > 3:
        score -= 1
    
    # Readability (simple heuristic: avg sentence length)
    sentences = re.split(r'[.!?]+', text)
    valid_sentences = [s for s in sentences if len(s.strip()) > 10]
    if valid_sentences:
        avg_length = sum(len(s.split()) for s in valid_sentences) / len(valid_sentences)
        if avg_length > 30:  # Too complex
            score -= 1
    
    return max(min(score, 10), 0)

def review_article(markdown_content):
    """Full quality review pipeline"""
    
    # Extract body (remove frontmatter)
    parts = markdown_content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = parts[2]
    else:
        frontmatter = ""
        body = markdown_content
    
    # Humanize
    body_humanized = humanize_text(body)
    
    # Score
    quality_score = score_quality(body_humanized)
    
    # Check structure
    issues, has_lists = check_structure(body_humanized)
    
    # Rebuild
    if frontmatter:
        final_content = f"---{frontmatter}---{body_humanized}"
    else:
        final_content = body_humanized
    
    return {
        'content': final_content,
        'quality_score': quality_score,
        'issues': issues,
        'has_lists': has_lists,
        'word_count': len(body_humanized.split())
    }

if __name__ == "__main__":
    # Test
    test_article = """---
title: Test
---

En conclusión, este es un artículo de prueba. Cabe destacar que tiene patrones de IA.

## Sección Test

Es importante señalar que la calidad importa. Sin duda, debemos verificar esto.
"""
    
    result = review_article(test_article)
    print(f"Quality score: {result['quality_score']}/10")
    print(f"Word count: {result['word_count']}")
    print(f"Issues: {result['issues']}")
    print("\nCleaned content preview:")
    print(result['content'][:300])

#!/usr/bin/env python3
"""Generate article hero images with DALL-E 3"""

import os
import requests
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

REPO_PATH = Path(__file__).parent.parent
IMAGE_DIR = REPO_PATH / 'public' / 'images' / 'articles'

def ensure_image_dir():
    """Create images directory if needed"""
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

def generate_article_image(title, slug, category='news'):
    """Generate hero image for article using DALL-E 3"""
    
    ensure_image_dir()
    
    # Build prompt for tech/AI editorial style
    prompt = build_dalle_prompt(title, category)
    
    print(f"  🎨 Generating image: {prompt[:60]}...")
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1792x1024",  # Wide format (editorial style)
            quality="standard",  # Standard = $0.04, HD = $0.08
            n=1,
        )
        
        image_url = response.data[0].url
        
        # Download image
        image_data = requests.get(image_url, timeout=30).content
        
        # Save locally
        image_path = IMAGE_DIR / f"{slug}.png"
        image_path.write_bytes(image_data)
        
        # Return relative path for frontmatter
        relative_path = f"/images/articles/{slug}.png"
        
        print(f"  ✓ Image saved: {relative_path}")
        return relative_path
        
    except Exception as e:
        print(f"  ✗ Image generation failed: {e}")
        return None

def build_dalle_prompt(title, category):
    """Build DALL-E prompt for editorial tech/AI image"""
    
    # Extract key concept from title
    title_clean = title.lower()
    
    # Base style
    style = "Modern editorial illustration, flat design, minimalist tech aesthetic"
    
    # Category-specific themes
    themes = {
        'news': 'futuristic interface, holographic elements, clean geometric shapes',
        'tutorial': 'educational diagram, step-by-step visual, instructional design',
        'review': 'product showcase, comparison layout, professional evaluation',
        'caso-de-uso': 'real-world application, success story visual, practical demonstration'
    }
    
    theme = themes.get(category, themes['news'])
    
    # Build prompt
    prompt = f"""{style}. {theme}. Color palette: deep blacks, soft grays, accent pink (#EC4899). 
Topic: {title}. 
Abstract representation, NO text, NO people faces, professional tech publication quality."""
    
    return prompt[:1000]  # DALL-E limit

def test_generation():
    """Test image generation"""
    
    test_title = "Gemini 3.1 Flash Live: audio IA más natural"
    test_slug = "test-dalle-generation"
    
    print(f"🧪 Testing DALL-E generation...")
    print(f"Title: {test_title}")
    
    image_path = generate_article_image(test_title, test_slug, 'news')
    
    if image_path:
        print(f"\n✅ SUCCESS!")
        print(f"Image: {image_path}")
        print(f"Cost: ~$0.04")
    else:
        print(f"\n✗ FAILED")

if __name__ == "__main__":
    test_generation()

#!/usr/bin/env python3
"""
Generate images using Google Gemini Imagen API
Usage: python3 generate_image.py "prompt text" output.png
"""

import sys
import os
import requests
import json

GEMINI_API_KEY = "AIzaSyD6m56ySGiImUIMHDo-O1QYNrN8YwbDEvM"

# Gemini models for image generation (2026)
MODELS = {
    "nanobanana": "gemini-2.5-flash-image",       # $0.039/image, ~500 free/day
    "nanobanana2": "gemini-3.1-flash-image-preview",  # $0.045/image @ 1K, ~500 free/day
    "imagen4-fast": "imagen-4.0-fast-generate-001",   # $0.02/image, NO free tier
    "imagen4": "imagen-4.0-generate-001",              # $0.04/image, NO free tier
}

DEFAULT_MODEL = "nanobanana2"  # Free tier, good quality

def generate_image(prompt, output_path, aspect_ratio="16:9", model=DEFAULT_MODEL):
    """
    Generate image using Gemini Imagen API
    
    Args:
        prompt: Text description of image to generate
        output_path: Where to save the generated image
        aspect_ratio: "1:1", "16:9", "9:16", "4:3", "3:4"
        model: Model to use (nanobanana, nanobanana2, imagen4-fast, imagen4)
    """
    
    model_id = MODELS.get(model, MODELS[DEFAULT_MODEL])
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateImages"
    
    # Map aspect ratios to pixel dimensions
    dimensions = {
        "1:1": {"width": 1024, "height": 1024},
        "16:9": {"width": 1792, "height": 1008},
        "9:16": {"width": 1008, "height": 1792},
        "4:3": {"width": 1536, "height": 1152},
        "3:4": {"width": 1152, "height": 1536}
    }
    
    size = dimensions.get(aspect_ratio, dimensions["16:9"])
    
    # Prepare request
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "number_of_images": 1,
        "aspect_ratio": aspect_ratio,
        "negative_prompt": "blurry, low quality, distorted, cartoon, text overlay, watermark"
    }
    
    url = f"{endpoint}?key={GEMINI_API_KEY}"
    
    try:
        print(f"🎨 Generating image with prompt: {prompt[:80]}...")
        print(f"📐 Aspect ratio: {aspect_ratio}")
        print(f"🤖 Model: {model_id}")
        
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Extract image data (base64)
        if "generatedImages" in result and len(result["generatedImages"]) > 0:
            import base64
            generated_image = result["generatedImages"][0]
            
            # Gemini returns base64 in "imageBytes" field
            if "imageBytes" in generated_image:
                image_data = base64.b64decode(generated_image["imageBytes"])
                
                with open(output_path, 'wb') as f:
                    f.write(image_data)
                
                print(f"✅ Image saved to: {output_path}")
                print(f"📊 Size: {len(image_data)} bytes ({len(image_data)/1024:.1f} KB)")
                return True
            else:
                print(f"❌ No imageBytes in response: {generated_image.keys()}")
                return False
        else:
            print(f"❌ No generatedImages in response: {result.keys()}")
            print(f"Response: {json.dumps(result, indent=2)[:500]}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image.py 'prompt text' output.png [aspect_ratio]")
        print("Aspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4 (default: 16:9)")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "16:9"
    
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    success = generate_image(prompt, output_path, aspect_ratio)
    sys.exit(0 if success else 1)

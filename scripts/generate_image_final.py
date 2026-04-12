#!/usr/bin/env python3
"""
Generate images using Google Gemini Imagen
Uses official google-genai SDK (2026)
"""

import sys
import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

GEMINI_API_KEY = "AIzaSyD6m56ySGiImUIMHDo-O1QYNrN8YwbDEvM"

# Available models (2026)
MODELS = {
    "nanobanana": "gemini-2.5-flash-image",              # Free tier, good quality
    "nanobanana2": "gemini-3.1-flash-image-preview",     # Free tier, latest
    "imagen4-fast": "imagen-4.0-fast-generate-001",      # $0.02/image, fastest
    "imagen4": "imagen-4.0-generate-001",                 # $0.04/image, standard
    "imagen4-ultra": "imagen-4.0-ultra-generate-001",    # $0.06/image, best quality
}

DEFAULT_MODEL = "nanobanana2"  # Free tier, latest model

def generate_image(prompt, output_path, aspect_ratio="16:9", model=DEFAULT_MODEL, num_images=1):
    """
    Generate image using Gemini Imagen
    
    Args:
        prompt: Text description
        output_path: Save path
        aspect_ratio: "1:1", "16:9", "9:16", "4:3", "3:4"
        model: Model name (nanobanana, nanobanana2, imagen4-fast, imagen4, imagen4-ultra)
        num_images: Number of images to generate (saves first one)
    """
    
    model_id = MODELS.get(model, MODELS[DEFAULT_MODEL])
    
    try:
        print(f"🎨 Generating image...")
        print(f"📝 Prompt: {prompt[:100]}...")
        print(f"📐 Aspect: {aspect_ratio}")
        print(f"🤖 Model: {model_id}")
        
        # Initialize client
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Generate images
        response = client.models.generate_images(
            model=model_id,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=num_images,
                aspect_ratio=aspect_ratio,
                safety_filter_level="block_low_and_above",
                person_generation="allow_adult"
            )
        )
        
        if response.generated_images and len(response.generated_images) > 0:
            # Get first generated image
            generated_image = response.generated_images[0]
            
            # Save to file
            generated_image.image.save(output_path)
            
            size = os.path.getsize(output_path)
            print(f"✅ Image saved to: {output_path}")
            print(f"📊 Size: {size/1024:.1f} KB")
            return True
        else:
            print("❌ No images generated")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Error type: {type(e).__name__}")
        
        # Try to get more error details
        if hasattr(e, 'message'):
            print(f"Message: {e.message}")
        if hasattr(e, 'details'):
            print(f"Details: {e.details}")
        
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image_final.py 'prompt' output.png [aspect_ratio] [model]")
        print("\nAspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4 (default: 16:9)")
        print("\nModels:")
        for name, model_id in MODELS.items():
            print(f"  {name}: {model_id}")
        print(f"\nDefault model: {DEFAULT_MODEL}")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "16:9"
    model = sys.argv[4] if len(sys.argv) > 4 else DEFAULT_MODEL
    
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    success = generate_image(prompt, output_path, aspect_ratio, model)
    sys.exit(0 if success else 1)

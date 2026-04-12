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

# ⚠️ SECURITY: ALWAYS use environment variable for API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("❌ Error: GEMINI_API_KEY not found in environment")
    print("   Set it with: export GEMINI_API_KEY='your_key_here'")
    print("   Or add to .env file (git-ignored)")
    sys.exit(1)

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
        prompt: Text description of image
        output_path: Where to save image
        aspect_ratio: One of: 1:1, 16:9, 9:16, 4:3, 3:4
        model: Model shorthand (nanobanana, imagen4-fast, etc.)
        num_images: Number of images to generate (1-4)
    """
    try:
        # Map shorthand to full model name
        model_name = MODELS.get(model, model)
        
        print(f"🎨 Generating image...")
        print(f"📝 Prompt: {prompt[:100]}...")
        print(f"📐 Aspect: {aspect_ratio}")
        print(f"🤖 Model: {model_name}")
        
        # Initialize client
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Configure generation
        config = types.GenerateImageConfig(
            number_of_images=num_images,
            aspect_ratio=aspect_ratio,
            safety_filter_level="block_low_and_above",  # Enum: block_low_and_above
            person_generation="allow_adult"  # Allow people in images
        )
        
        # Generate
        response = client.models.generate_image(
            model=model_name,
            prompt=prompt,
            config=config
        )
        
        # Save first image
        if response.generated_images:
            img_data = response.generated_images[0]._image
            
            # Convert to PIL Image
            image = Image.open(BytesIO(img_data))
            
            # Create output directory if needed
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
            
            # Save
            image.save(output_path)
            
            # Get file size
            size_kb = os.path.getsize(output_path) / 1024
            
            print(f"✅ Image saved to: {output_path}")
            print(f"📊 Size: {size_kb:.1f} KB")
            return True
        else:
            print("❌ No images generated")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image_final.py <prompt> <output_path> [aspect_ratio] [model]")
        print()
        print("Examples:")
        print('  python3 generate_image_final.py "sunset over mountains" output.png')
        print('  python3 generate_image_final.py "cat on couch" cat.jpg "1:1" "imagen4-fast"')
        print()
        print("Available models:")
        for key, value in MODELS.items():
            print(f"  {key:15} → {value}")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "16:9"
    model = sys.argv[4] if len(sys.argv) > 4 else DEFAULT_MODEL
    
    success = generate_image(prompt, output_path, aspect_ratio, model)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate images using Google Gemini Imagen (Nano Banana 2)
Official SDK method
"""

import sys
import os
import google.generativeai as genai
from PIL import Image
import io

GEMINI_API_KEY = "AIzaSyD6m56ySGiImUIMHDo-O1QYNrN8YwbDEvM"

def generate_image(prompt, output_path, aspect_ratio="16:9"):
    """
    Generate image using Gemini Imagen 3 (Nano Banana 2)
    
    Args:
        prompt: Text description
        output_path: Save path
        aspect_ratio: "1:1", "16:9", "9:16", "4:3", "3:4"
    """
    
    genai.configure(api_key=GEMINI_API_KEY)
    
    try:
        print(f"🎨 Generating with Nano Banana 2...")
        print(f"📝 Prompt: {prompt[:100]}...")
        print(f"📐 Aspect: {aspect_ratio}")
        
        # Use imagen-3.0-generate-001 model
        model = genai.ImageGenerationModel("imagen-3.0-generate-001")
        
        result = model.generate_images(
            prompt=prompt,
            number_of_images=1,
            aspect_ratio=aspect_ratio,
            safety_filter_level="block_only_high",
            person_generation="allow_adult"
        )
        
        if result.images:
            # Save first generated image
            image = result.images[0]
            image._pil_image.save(output_path)
            
            size = os.path.getsize(output_path)
            print(f"✅ Saved: {output_path}")
            print(f"📊 Size: {size/1024:.1f} KB")
            return True
        else:
            print("❌ No images generated")
            return False
            
    except AttributeError:
        # Fallback: try different API structure
        print("⚠️  Trying alternate API method...")
        try:
            model = genai.GenerativeModel("gemini-3.1-flash-image-preview")
            response = model.generate_content([prompt])
            
            # Extract image from response
            if hasattr(response, 'images') and response.images:
                response.images[0].save(output_path)
                print(f"✅ Saved: {output_path}")
                return True
            else:
                print(f"❌ No images in response")
                print(f"Response type: {type(response)}")
                print(f"Response: {response}")
                return False
                
        except Exception as e2:
            print(f"❌ Alternate method failed: {e2}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Error type: {type(e).__name__}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image_gemini.py 'prompt' output.png [aspect_ratio]")
        print("Aspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "16:9"
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    success = generate_image(prompt, output_path, aspect_ratio)
    sys.exit(0 if success else 1)

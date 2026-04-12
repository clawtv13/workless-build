#!/usr/bin/env python3
"""Generate default OG image for WorkLess.build"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create 1200x630 image (OG standard)
width, height = 1200, 630
bg_color = (13, 17, 28)  # Dark background
primary_color = (102, 126, 234)  # Purple
accent_color = (118, 75, 162)  # Accent purple

img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Gradient effect (simple vertical)
for y in range(height):
    mix = y / height
    r = int(bg_color[0] + (accent_color[0] - bg_color[0]) * mix)
    g = int(bg_color[1] + (accent_color[1] - bg_color[1]) * mix)
    b = int(bg_color[2] + (accent_color[2] - bg_color[2]) * mix)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Try to load font, fallback to default
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 96)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
except:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()

# Draw text
title = "WorkLess AI"
subtitle = "La fuente definitiva de IA en español"

# Center text
bbox_title = draw.textbbox((0, 0), title, font=font_title)
title_width = bbox_title[2] - bbox_title[0]
title_x = (width - title_width) // 2

bbox_subtitle = draw.textbbox((0, 0), subtitle, font=font_subtitle)
subtitle_width = bbox_subtitle[2] - bbox_subtitle[0]
subtitle_x = (width - subtitle_width) // 2

# Draw with shadow
draw.text((title_x + 4, 230 + 4), title, fill=(0, 0, 0, 128), font=font_title)
draw.text((title_x, 230), title, fill=primary_color, font=font_title)

draw.text((subtitle_x + 2, 360 + 2), subtitle, fill=(0, 0, 0, 128), font=font_subtitle)
draw.text((subtitle_x, 360), subtitle, fill=(200, 200, 220), font=font_subtitle)

# Save
output_path = os.path.join(os.path.dirname(__file__), '..', 'public', 'og-image.png')
img.save(output_path, 'PNG', optimize=True)
print(f"✅ OG image generated: {output_path}")

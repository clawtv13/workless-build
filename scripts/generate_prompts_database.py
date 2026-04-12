#!/usr/bin/env python3
"""
Generate 500+ prompts database using OpenRouter Claude API.
Generates in batches, combines into single JSON file.
"""

import json
import os
import requests
import time
from pathlib import Path

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    print("❌ Error: OPENROUTER_API_KEY not found in environment")
    print("   Set it with: export OPENROUTER_API_KEY='your_key_here'")
    print("   Or add to .env file in project root")
    sys.exit(1)

MODEL = "anthropic/claude-sonnet-4"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Categories configuration
CATEGORIES = {
    "marketing": {
        "subcategories": ["email", "social_media", "ads_copy", "seo", "content"],
        "sectors": ["retail", "saas", "servicios", "hostelería", "ecommerce"],
        "count": 100
    },
    "servicios_profesionales": {
        "subcategories": ["informes", "research", "presentaciones", "analisis", "documentacion"],
        "sectors": ["gestoría", "consultoría", "asesoría", "agencia"],
        "count": 100
    },
    "legal": {
        "subcategories": ["contratos", "research_juridico", "compliance", "documentos", "resumenes"],
        "sectors": ["bufete", "asesoría_laboral", "notaría", "legal"],
        "count": 100
    },
    "retail": {
        "subcategories": ["descripciones_producto", "atencion_cliente", "marketing_retail", "gestion_inventario", "reviews"],
        "sectors": ["tienda_online", "retail_fisico", "dropshipping", "marketplace"],
        "count": 100
    },
    "hosteleria": {
        "subcategories": ["menus", "marketing_hosteleria", "reservas", "atencion_cliente", "gestion_operativa"],
        "sectors": ["restaurante", "hotel", "cafetería", "bar", "catering"],
        "count": 100
    }
}

def generate_prompts_batch(category, batch_size=20):
    """Generate prompts for a category in batches."""
    
    config = CATEGORIES[category]
    subcategories = config["subcategories"]
    sectors = config["sectors"]
    total = config["count"]
    
    system_prompt = f"""Eres un experto en prompts de IA para empresas españolas.

Genera {batch_size} prompts profesionales para la categoría: {category}

ESTRUCTURA JSON EXACTA:
{{
  "id": número,
  "title": "Título breve español",
  "prompt": "Prompt detallado con [PLACEHOLDERS] para personalizar",
  "category": "{category}",
  "subcategory": "una de {subcategories}",
  "sector": "uno de {sectors}",
  "llm": "ChatGPT" o "Claude" o "Gemini",
  "difficulty": "basico" o "intermedio" o "avanzado",
  "tags": ["tag1", "tag2", "tag3"],
  "use_case": "Descripción caso uso específico",
  "example_output": "Ejemplo salida corto"
}}

REGLAS:
- TODOS los prompts en español
- Prompts específicos (industria, tono, formato)
- Incluye [PLACEHOLDERS] para personalizar
- Mix difficulty: 33% básico, 34% intermedio, 33% avanzado
- Mix LLM: 40% ChatGPT, 30% Claude, 30% Gemini
- Varía sectores
- Actionable (copy-paste ready)

Genera {batch_size} prompts ahora. SOLO JSON array, sin explicaciones."""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Genera {batch_size} prompts ahora en formato JSON array."}
        ],
        "temperature": 0.7,
        "max_tokens": 8000
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        
        content = response.json()["choices"][0]["message"]["content"]
        
        # Extract JSON from markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        prompts = json.loads(content)
        return prompts
        
    except Exception as e:
        print(f"❌ Error generating batch: {e}")
        return []

def generate_all_prompts():
    """Generate all 500 prompts."""
    
    all_prompts = []
    prompt_id = 1
    
    for category, config in CATEGORIES.items():
        print(f"\n🎯 Generando {config['count']} prompts para: {category}")
        
        category_prompts = []
        batches_needed = config['count'] // 20
        
        for batch_num in range(batches_needed):
            print(f"  Batch {batch_num + 1}/{batches_needed}...", end=" ", flush=True)
            
            batch = generate_prompts_batch(category, batch_size=20)
            
            if batch:
                # Fix IDs to be sequential
                for prompt in batch:
                    prompt['id'] = prompt_id
                    prompt_id += 1
                    category_prompts.append(prompt)
                
                print(f"✅ {len(batch)} prompts")
            else:
                print("❌ Failed")
            
            # Rate limiting
            time.sleep(2)
        
        all_prompts.extend(category_prompts)
        print(f"  ✅ Total {category}: {len(category_prompts)} prompts\n")
    
    return all_prompts

def save_database(prompts, output_path):
    """Save prompts to JSON file."""
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    database = {"prompts": prompts}
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Database saved: {output_path}")
    print(f"📊 Total prompts: {len(prompts)}")

def main():
    """Main execution."""
    
    print("🚀 Generating 500+ prompts database...\n")
    
    output_path = "/root/.openclaw/workspace/workless-v2/public/data/prompts-database.json"
    
    prompts = generate_all_prompts()
    
    if prompts:
        save_database(prompts, output_path)
        
        # Stats
        by_category = {}
        by_difficulty = {}
        by_llm = {}
        
        for p in prompts:
            cat = p.get('category', 'unknown')
            diff = p.get('difficulty', 'unknown')
            llm = p.get('llm', 'unknown')
            
            by_category[cat] = by_category.get(cat, 0) + 1
            by_difficulty[diff] = by_difficulty.get(diff, 0) + 1
            by_llm[llm] = by_llm.get(llm, 0) + 1
        
        print("\n📊 Statistics:")
        print(f"  By category: {by_category}")
        print(f"  By difficulty: {by_difficulty}")
        print(f"  By LLM: {by_llm}")
    else:
        print("❌ No prompts generated")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())

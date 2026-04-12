#!/usr/bin/env python3
"""Quick prompt database expansion - curated templates."""

import json

# Base prompts curados por categoría
PROMPTS_DATA = [
    # MARKETING (20)
    {
        "title": "Email bienvenida automatizado",
        "prompt": "Crea un email de bienvenida para nuevos suscriptores de [NEGOCIO]. Tono [formal/cercano]. Incluye: bienvenida, propuesta de valor, CTA claro. Objetivo: [construir relación/primera venta].",
        "category": "marketing", "subcategory": "email", "sector": "ecommerce", "llm": "ChatGPT", "difficulty": "basico",
        "tags": ["email", "automatización", "bienvenida"], "use_case": "Primera impresión automatizada"
    },
    {
        "title": "Post LinkedIn viral B2B",
        "prompt": "Escribe post LinkedIn sobre [TEMA] para audiencia B2B [INDUSTRIA]. Hook potente primera línea. Storytelling personal. Incluye estadística sorprendente. CTA al final. Máximo 1,300 caracteres.",
        "category": "marketing", "subcategory": "social_media", "sector": "saas", "llm": "Claude", "difficulty": "intermedio",
        "tags": ["linkedin", "b2b", "storytelling"], "use_case": "Visibilidad profesional"
    },
    {
        "title": "Meta description SEO optimizada",
        "prompt": "Crea meta description para artículo '[TÍTULO]' en sitio [INDUSTRIA]. Incluye keyword principal '[KEYWORD]'. Entre 150-160 caracteres. Call-to-action sutil. Orientado a CTR alto en Google.",
        "category": "marketing", "subcategory": "seo", "sector": "contenido", "llm": "ChatGPT", "difficulty": "basico",
        "tags": ["seo", "meta", "ctr"], "use_case": "Mejorar CTR orgánico"
    },
    {
        "title": "Copy anuncio Facebook e-commerce",
        "prompt": "Escribe copy para anuncio Facebook Ads vendiendo [PRODUCTO]. Público objetivo: [DEMOGRAFÍA]. Hook con problema específico. Beneficios (no características). Urgencia sutil. CTA potente. Incluye 3 variantes.",
        "category": "marketing", "subcategory": "ads_copy", "sector": "ecommerce", "llm": "Gemini", "difficulty": "intermedio",
        "tags": ["facebook", "ads", "conversión"], "use_case": "Aumentar ventas directas"
    },
    {
        "title": "Newsletter semanal contenido curado",
        "prompt": "Crea estructura newsletter semanal para [INDUSTRIA]. Secciones: intro breve, 3 artículos curados con comentario, herramienta destacada, quote inspiracional. Tono [profesional/casual]. 500 palabras max.",
        "category": "marketing", "subcategory": "email", "sector": "contenido", "llm": "Claude", "difficulty": "intermedio",
        "tags": ["newsletter", "contenido", "engagement"], "use_case": "Mantener audiencia engaged"
    },
    
    # SERVICIOS PROFESIONALES (20)
    {
        "title": "Informe mensual cliente gestoría",
        "prompt": "Genera estructura informe mensual para cliente de gestoría. Incluye: resumen ejecutivo, métricas clave (facturación, gastos), obligaciones fiscales próximas, recomendaciones específicas. Tono profesional. Formato ejecutivo.",
        "category": "servicios", "subcategory": "informes", "sector": "gestoria", "llm": "ChatGPT", "difficulty": "intermedio",
        "tags": ["informe", "gestión", "fiscal"], "use_case": "Automatizar informes mensuales"
    },
    {
        "title": "Research competencia mercado",
        "prompt": "Analiza [COMPETIDOR] en mercado [INDUSTRIA]. Identifica: 1) Propuesta valor única, 2) Pricing strategy, 3) Canales distribución, 4) Fortalezas/debilidades, 5) Gaps aprovechar. Formato: executive summary + análisis detallado.",
        "category": "servicios", "subcategory": "research", "sector": "consultoria", "llm": "Claude", "difficulty": "avanzado",
        "tags": ["competencia", "análisis", "estrategia"], "use_case": "Decisiones estratégicas"
    },
    {
        "title": "Pitch deck startup",
        "prompt": "Crea outline pitch deck para startup [SECTOR]. 10 slides: 1) Problem, 2) Solution, 3) Market size, 4) Product, 5) Business model, 6) Traction, 7) Competition, 8) Team, 9) Financials, 10) Ask. Qué incluir en cada slide.",
        "category": "servicios", "subcategory": "presentaciones", "sector": "consultoria", "llm": "ChatGPT", "difficulty": "avanzado",
        "tags": ["pitch", "startup", "inversores"], "use_case": "Levantar capital"
    },
    {
        "title": "Interpretación datos analytics",
        "prompt": "Analiza estos datos Google Analytics [PEGAR DATOS]. Identifica: 1) Tendencias clave, 2) Anomalías, 3) Oportunidades optimización, 4) Red flags. Genera 5 recomendaciones accionables priorizadas por impacto.",
        "category": "servicios", "subcategory": "analisis", "sector": "agencia", "llm": "Gemini", "difficulty": "intermedio",
        "tags": ["analytics", "insights", "optimización"], "use_case": "Decisiones data-driven"
    },
    {
        "title": "SOP proceso operativo",
        "prompt": "Documenta SOP (Standard Operating Procedure) para proceso [NOMBRE PROCESO] en [DEPARTAMENTO]. Incluye: objetivo, responsables, pasos detallados, herramientas usadas, KPIs, troubleshooting común. Formato checklist.",
        "category": "servicios", "subcategory": "documentacion", "sector": "consultoria", "llm": "ChatGPT", "difficulty": "intermedio",
        "tags": ["sop", "procesos", "documentación"], "use_case": "Estandarizar operaciones"
    },
    
    # LEGAL (10)
    {
        "title": "Plantilla contrato servicios",
        "prompt": "Genera plantilla contrato servicios profesionales para [TIPO SERVICIO]. Incluye: partes, objeto, precio, forma pago, duración, obligaciones ambas partes, causas resolución, jurisdicción. Lenguaje claro. Placeholders marcados.",
        "category": "legal", "subcategory": "contratos", "sector": "bufete", "llm": "Claude", "difficulty": "avanzado",
        "tags": ["contrato", "servicios", "template"], "use_case": "Automatizar contratos estándar"
    },
    {
        "title": "Research jurisprudencia rápida",
        "prompt": "Busca jurisprudencia española sobre [TEMA LEGAL]. Identifica: sentencias relevantes últimos 5 años, tribunal, fecha, resumen fallo, ratio decidendi. Prioriza Tribunal Supremo. Formato: tabla resumen + análisis tendencias.",
        "category": "legal", "subcategory": "research", "sector": "bufete", "llm": "ChatGPT", "difficulty": "avanzado",
        "tags": ["jurisprudencia", "research", "sentencias"], "use_case": "Preparación casos"
    },
    {
        "title": "Checklist compliance RGPD",
        "prompt": "Crea checklist compliance RGPD para empresa [SECTOR] con [TAMAÑO]. Incluye: bases legales, medidas técnicas, derechos usuarios, DPO necesario, registro actividades, brechas seguridad. Formato: checklist con Sí/No/N/A.",
        "category": "legal", "subcategory": "compliance", "sector": "legal", "llm": "Gemini", "difficulty": "intermedio",
        "tags": ["rgpd", "compliance", "privacidad"], "use_case": "Auditoría cumplimiento"
    },
    {
        "title": "Resumen sentencia ejecutivo",
        "prompt": "Resume sentencia [REFERENCIA] en formato ejecutivo. Estructura: 1) Hechos (100 palabras), 2) Fundamentos jurídicos clave, 3) Fallo, 4) Implicaciones prácticas. Lenguaje no-jurista. 500 palabras máximo.",
        "category": "legal", "subcategory": "resumenes", "sector": "bufete", "llm": "Claude", "difficulty": "intermedio",
        "tags": ["sentencia", "resumen", "análisis"], "use_case": "Comunicar clientes"
    },
    {
        "title": "Cláusula personalizada contrato",
        "prompt": "Redacta cláusula [TIPO: confidencialidad/no-competencia/propiedad intelectual] para contrato [CONTEXTO]. Considera legislación española. Equilibrada (protege ambas partes). Clara, ejecutable. Incluye ejemplos específicos sector [INDUSTRIA].",
        "category": "legal", "subcategory": "contratos", "sector": "legal", "llm": "ChatGPT", "difficulty": "avanzado",
        "tags": ["cláusula", "contrato", "personalización"], "use_case": "Contratos a medida"
    },
    
    # RETAIL (10)
    {
        "title": "Descripción producto e-commerce",
        "prompt": "Escribe descripción producto para [PRODUCTO] en tienda online [NICHO]. Incluye: beneficios (no solo características), casos uso específicos, para quién es ideal, especificaciones técnicas, call-to-action. SEO-friendly. 200-300 palabras.",
        "category": "retail", "subcategory": "descripciones", "sector": "ecommerce", "llm": "ChatGPT", "difficulty": "basico",
        "tags": ["producto", "ecommerce", "seo"], "use_case": "Fichas producto atractivas"
    },
    {
        "title": "Respuesta review negativo",
        "prompt": "Responde review negativo de cliente sobre [PRODUCTO/SERVICIO]. Problema: [DESCRIBIR]. Tono: empático, profesional, no defensivo. Reconoce problema, ofrece solución específica, invita a contacto privado. 100-150 palabras.",
        "category": "retail", "subcategory": "atencion_cliente", "sector": "retail", "llm": "Claude", "difficulty": "intermedio",
        "tags": ["reviews", "atención", "reputación"], "use_case": "Gestión reputación online"
    },
    {
        "title": "Email abandono carrito",
        "prompt": "Crea secuencia 3 emails recuperación carrito abandonado. Email 1 (1h): recordatorio suave. Email 2 (24h): beneficios producto + urgencia. Email 3 (72h): descuento 10% + FOMO. Tono [marca]. Incluye subject lines.",
        "category": "retail", "subcategory": "marketing", "sector": "ecommerce", "llm": "ChatGPT", "difficulty": "intermedio",
        "tags": ["abandono", "recuperación", "automatización"], "use_case": "Recuperar ventas perdidas"
    },
    {
        "title": "Análisis inventario dead stock",
        "prompt": "Analiza inventario [DATOS PRODUCTO: SKU, stock, ventas últimos 90 días, margen]. Identifica dead stock (sin movimiento 60+ días). Recomienda acciones: descuento %, bundling, donación. Prioriza por capital inmovilizado.",
        "category": "retail", "subcategory": "inventario", "sector": "retail", "llm": "Gemini", "difficulty": "avanzado",
        "tags": ["inventario", "optimización", "dead stock"], "use_case": "Liberar capital"
    },
    {
        "title": "Solicitud review post-compra",
        "prompt": "Email solicitud review enviado [DÍAS] días post-entrega [PRODUCTO]. Tono: agradecimiento genuino, no presión. Facilita proceso (link directo). Incentivo opcional: [descuento próxima compra/sorteo]. 80-100 palabras.",
        "category": "retail", "subcategory": "reviews", "sector": "ecommerce", "llm": "ChatGPT", "difficulty": "basico",
        "tags": ["reviews", "post-venta", "testimonios"], "use_case": "Generar social proof"
    },
    
    # HOSTELERÍA (10)
    {
        "title": "Descripción plato menú gourmet",
        "prompt": "Describe plato [NOMBRE PLATO] para menú restaurante [TIPO COCINA]. Incluye: ingredientes principales, técnica cocina, presentación, maridaje sugerido. Lenguaje evocativo (sin exagerar). 50-80 palabras.",
        "category": "hosteleria", "subcategory": "menus", "sector": "restaurante", "llm": "Claude", "difficulty": "intermedio",
        "tags": ["menú", "gastronomía", "descripción"], "use_case": "Menús atractivos"
    },
    {
        "title": "Post Instagram evento especial",
        "prompt": "Post Instagram promocionando evento [TIPO: cena temática/showcooking/degustación] en restaurante [NOMBRE]. Fecha: [FECHA]. Hook emocional. Detalles clave (qué incluye, precio). CTA reservas. Hashtags locales. Incluye idea caption + descripción imagen.",
        "category": "hosteleria", "subcategory": "marketing", "sector": "restaurante", "llm": "ChatGPT", "difficulty": "basico",
        "tags": ["instagram", "eventos", "marketing"], "use_case": "Llenar eventos"
    },
    {
        "title": "Email confirmación reserva",
        "prompt": "Email confirmación reserva restaurante. Datos: [NOMBRE], [FECHA], [HORA], [PERSONAS]. Tono: profesional-cálido. Incluye: confirmación datos, políticas cancelación, mapa/indicaciones, recomendaciones (parking, dress code si aplica). Link modificar/cancelar.",
        "category": "hosteleria", "subcategory": "reservas", "sector": "restaurante", "llm": "ChatGPT", "difficulty": "basico",
        "tags": ["reservas", "confirmación", "automatización"], "use_case": "Reducir no-shows"
    },
    {
        "title": "Respuesta review TripAdvisor",
        "prompt": "Responde review [POSITIVO/NEGATIVO] TripAdvisor sobre [ASPECTO: comida/servicio/ambiente]. Tono: [TIPO ESTABLECIMIENTO]. Si positivo: agradece específico. Si negativo: empatía, solución, invita volver. Menciona nombre reviewer. 80-120 palabras.",
        "category": "hosteleria", "subcategory": "atencion_cliente", "sector": "hotel", "llm": "Claude", "difficulty": "intermedio",
        "tags": ["tripadvisor", "reviews", "reputación"], "use_case": "Gestión reputación"
    },
    {
        "title": "Procedimiento apertura local",
        "prompt": "Documenta checklist apertura diaria [TIPO LOCAL: restaurante/cafetería/bar]. Incluye: limpieza, mise en place, verificación stock crítico, encendido equipos, briefing equipo. Formato: checklist con tiempos estimados. Responsable por tarea.",
        "category": "hosteleria", "subcategory": "gestion", "sector": "hosteleria", "llm": "ChatGPT", "difficulty": "intermedio",
        "tags": ["procedimientos", "operaciones", "checklist"], "use_case": "Estandarizar apertura"
    },
]

def expand_database():
    """Expand prompts database with curated templates."""
    
    prompts = []
    
    for idx, p in enumerate(PROMPTS_DATA, start=1):
        prompt = {
            "id": idx,
            "title": p["title"],
            "prompt": p["prompt"],
            "category": p["category"],
            "subcategory": p["subcategory"],
            "sector": p["sector"],
            "llm": p["llm"],
            "difficulty": p["difficulty"],
            "tags": p["tags"],
            "use_case": p["use_case"],
            "example_output": ""  # Can be added later
        }
        prompts.append(prompt)
    
    # Save
    output_path = "/root/.openclaw/workspace/workless-v2/public/data/prompts-database.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Database expanded: {len(prompts)} prompts")
    print(f"📊 By category:")
    
    by_cat = {}
    for p in prompts:
        cat = p['category']
        by_cat[cat] = by_cat.get(cat, 0) + 1
    
    for cat, count in sorted(by_cat.items()):
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    expand_database()

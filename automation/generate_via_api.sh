#!/bin/bash
# Generate article content via API call
# Usage: ./generate_via_api.sh "title" "summary" "source"

TITLE="$1"
SUMMARY="$2"
SOURCE="$3"

PROMPT="Eres periodista tech especializado en IA escribiendo para WorkLess.build.

NOTICIA:
Título: $TITLE
Resumen: $SUMMARY
Fuente: $SOURCE

Escribe artículo español (España, 400-600 palabras).

ESTRUCTURA:
- Lead paragraph (qué + por qué importa)
- 2-3 secciones ## Headers
- Bullets para listas
- Párrafos cortos
- Conclusión actionable

TONO: Profesional, directo, sin hype.

Solo markdown (sin frontmatter YAML):
"

# Use OpenClaw's model access
echo "$PROMPT"

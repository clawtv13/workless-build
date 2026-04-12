# PART 3: MARCO REGULATORIO

## 3.1 AI Act: Qué Cambia en Agosto 2026

El 2 de agosto de 2026 marca un antes y un después en la inteligencia artificial europea. Ese día entra en vigor el grueso de obligaciones del **Reglamento UE 2024/1689** —conocido como AI Act—, la primera legislación del mundo que regula la IA de forma integral.

Para las empresas españolas, esto no es solo otro requisito de compliance. Es una redefinición completa de cómo se desarrolla, despliega y supervisa cualquier sistema de inteligencia artificial.

### El Enfoque Basado en Riesgo: Cuatro Categorías

El AI Act clasifica los sistemas de IA en cuatro niveles según su impacto potencial sobre derechos fundamentales y seguridad:

**1. Riesgo Inaceptable (Prohibido)**

Estos sistemas quedan prohibidos por completo en la UE. No hay excepciones comerciales:

- **Manipulación subliminal** que pueda causar daño físico o psicológico
- **Explotación de vulnerabilidades** por edad, discapacidad o situación socioeconómica
- **Social scoring** por parte de autoridades públicas (estilo crédito social chino)
- **Identificación biométrica remota en tiempo real** en espacios públicos (con excepciones muy limitadas para seguridad nacional)

Si tu sistema cae en esta categoría, no hay ruta de compliance posible. Simplemente no puedes operarlo.

**2. Alto Riesgo (Obligaciones Estrictas)**

Los sistemas de alto riesgo pueden usarse, pero están sujetos a obligaciones exhaustivas. Incluyen:

- Sistemas de **recursos humanos**: screening de CVs, evaluación de desempeño, decisiones de promoción
- **Scoring crediticio** y evaluación de solvencia
- **Infraestructuras críticas**: gestión de tráfico, suministro de agua/gas/electricidad
- **Educación**: herramientas que determinen acceso o calificaciones
- **Aplicación de la ley**: análisis de evidencias, predicción de reincidencia
- **Migración y fronteras**: verificación de documentos, detección de riesgos

¿Tu empresa usa un sistema de IA para filtrar candidatos en el proceso de selección? **Es alto riesgo**. ¿Implementas un chatbot que ayuda a evaluar solicitudes de crédito? **Alto riesgo también**.

Las obligaciones para estos sistemas son sustanciales:

**Documentación técnica exhaustiva** (Anexo IV del Reglamento):
- Descripción detallada del sistema y su finalidad
- Dataset de entrenamiento: origen, representatividad, método de recopilación
- Arquitectura del modelo y parámetros clave
- Métricas de rendimiento (precisión, recall, F1-score)
- Medidas contra sesgos y discriminación
- Procedimientos de evaluación de conformidad

**Registro obligatorio en base de datos de la UE**:
- Todos los sistemas de alto riesgo deben inscribirse en un registro público
- Información básica visible para usuarios y autoridades
- Actualización cuando hay cambios sustanciales

**Sistema de gestión de riesgos**:
- Identificación y análisis de riesgos conocidos y previsibles
- Medidas de mitigación
- Testing de situaciones de riesgo
- Revisión continua basada en uso real

**Gobernanza y calidad de datos**:
- Los datasets deben ser relevantes, representativos, libres de errores
- Examen en busca de sesgos (raza, género, edad, discapacidad)
- Documentación completa del data pipeline

**Supervisión humana efectiva**:
- Una persona debe poder intervenir en decisiones del sistema
- Capacidad de pausar o revertir decisiones automatizadas
- Formación adecuada para supervisores

**Ciberseguridad y robustez**:
- Protección contra ataques adversarios
- Resiliencia ante fallos técnicos
- Logging de eventos para auditorías

**Transparencia y trazabilidad**:
- Capacidad de explicar cómo se llegó a una decisión
- Logs automáticos de operaciones
- Información clara a usuarios afectados

El incumplimiento de estas obligaciones puede resultar en sanciones de **hasta 15 millones de euros o el 3% de la facturación global anual**, lo que sea mayor.

**3. Riesgo Limitado (Transparencia)**

Sistemas como chatbots, generadores de contenido o deepfakes deben cumplir **obligaciones de transparencia**:

- **Divulgar que es IA**: Los usuarios deben saber que están interactuando con un sistema automatizado
- **Contenido sintético**: Imágenes, audio o video generado por IA debe estar claramente etiquetado
- **Detección de manipulación**: Sistemas que identifican deepfakes deben ser transparentes sobre sus limitaciones

Si tu web tiene un chatbot de atención al cliente, necesitas un mensaje claro al inicio: *"Estás hablando con un asistente de IA. Para hablar con una persona, escribe 'agente humano'."*

Si tu herramienta de marketing genera imágenes con DALL-E o Midjourney para redes sociales, cada publicación debe indicar: *"Imagen generada con inteligencia artificial"*.

**4. Riesgo Mínimo (Sin Obligaciones Específicas)**

La mayoría de aplicaciones de IA caen aquí:

- Filtros de spam en email
- Recomendaciones de productos en e-commerce
- Videojuegos con IA
- Herramientas de productividad básicas

Estos sistemas no tienen requisitos específicos del AI Act, aunque siguen sujetos a GDPR, leyes de consumo y normativa general.

### ¿Quién Supervisa Todo Esto en España?

La **Agencia Española de Supervisión de la Inteligencia Artificial (AESIA)** fue creada en agosto de 2023 específicamente para este propósito.

AESIA tiene potestad para:

- Realizar **auditorías e inspecciones** de sistemas de IA
- Exigir documentación técnica
- Imponer **medidas correctivas** (desde advertencias hasta prohibiciones de uso)
- Aplicar **sanciones económicas** según el AI Act
- Coordinar con otras autoridades (AEPD para temas de privacidad, CNMC para competencia)

AESIA también gestiona el **sandbox regulatorio** (Real Decreto 817/2023), un entorno controlado donde empresas pueden probar sistemas de IA innovadores bajo supervisión, antes del despliegue completo. Si estás desarrollando algo nuevo y de alto riesgo, el sandbox puede ser tu mejor aliado para iterar con apoyo regulatorio.

### Las Multas: Cuánto Puede Costar el Incumplimiento

El AI Act establece un régimen de sanciones **proporcional pero contundente**:

- **Uso de sistemas prohibidos**: Hasta **35 millones de euros o 7% de la facturación global anual**
- **Incumplimiento de obligaciones de alto riesgo**: Hasta **15 millones de euros o 3% de facturación**
- **Información incorrecta a autoridades**: Hasta **7,5 millones de euros o 1,5% de facturación**

Para poner esto en perspectiva: una startup española de healthtech con €2M de facturación anual y un sistema de diagnóstico de alto riesgo no conforme podría enfrentar una multa de €60.000 (3%). Doloroso, pero no letal.

Pero una fintech con €50M de facturación y un sistema de scoring crediticio problemático podría recibir €1,5M de sanción. Eso sí puede quebrar una empresa mediana.

### El Impacto Real en Empresas Españolas

Según datos de Deloitte (2026), el **49% de empresas españolas** cita la regulación y la gobernanza como **barrera principal** para adoptar IA generativa. No es miedo irracional: es la realidad de que el compliance tiene un costo.

Pero también hay buenas noticias:

- **El 80% de empresas españolas** reporta **mayor confianza** en la IA desde la llegada del AI Act. La regulación clara reduce incertidumbre.
- Las **PYMEs tienen documentación simplificada**: el Anexo IV (documentación técnica) se ha adaptado para reducir carga burocrática en empresas pequeñas.
- **Gradualidad**: Las obligaciones entran en vigor de forma escalonada entre 2024 y 2027, dando tiempo para adaptarse.

La clave está en entender que el compliance no es un obstáculo, sino una **ventaja competitiva**. Las empresas españolas que dominen el AI Act antes que sus competidores europeos podrán:

- Vender servicios de IA con certificación de compliance
- Exportar soluciones a otros países de la UE con confianza
- Atraer clientes que valoran la transparencia y responsabilidad
- Evitar multas millonarias que pueden destruir el negocio

Agosto de 2026 no es el fin de la innovación en IA. Es el comienzo de una **era de IA responsable, auditable y confiable**.

---

## 3.2 Cómo Prepararse para el Compliance

El AI Act no es solo un documento legal de 400 páginas. Es una invitación a **transformar cómo tu empresa piensa sobre la IA**. Si lo ves como una checklist burocrática, fracasarás. Si lo ves como una oportunidad para construir sistemas más robustos, transparentes y confiables, saldrás adelante.

Aquí tienes una hoja de ruta práctica para preparar tu organización, paso a paso.

### Paso 1: Inventario Completo de Sistemas de IA

**Duración estimada: 2-4 semanas**

Antes de cumplir con el AI Act, necesitas saber **qué IA estás usando**. Muchas empresas subestiman esto y descubren tarde que tienen docenas de sistemas dispersos.

**Acciones concretas:**

1. **Audita todas las áreas de negocio**:
   - Marketing: ¿usas chatbots, generadores de contenido, herramientas de personalización?
   - RRHH: ¿filtras CVs con IA, evalúas desempeño con algoritmos?
   - Ventas: ¿scores de leads, predicción de churn?
   - Operaciones: ¿mantenimiento predictivo, optimización de rutas?
   - Finanzas: ¿detección de fraude, scoring crediticio?

2. **Incluye herramientas SaaS de terceros**:
   - ChatGPT embebido en tu web
   - HubSpot con predictive lead scoring
   - Zendesk con IA para ticketing
   - Aunque no hayas desarrollado el modelo, **eres responsable de su uso**

3. **Clasifica cada sistema por categoría de riesgo**:
   - ¿Afecta derechos fundamentales? → Probablemente alto riesgo
   - ¿Es solo automatización básica? → Riesgo mínimo
   - ¿Interactúa con usuarios finales? → Mínimo riesgo limitado (transparencia)

4. **Documenta cada sistema en una tabla**:
   - Nombre del sistema
   - Proveedor (interno o externo)
   - Finalidad
   - Datos que procesa
   - Categoría de riesgo (preliminar)
   - Responsable de negocio

**Resultado esperado**: Un inventario claro en Excel/Notion/Airtable con 100% de visibilidad sobre tu superficie de IA.

**Trampas comunes**:
- Olvidar sistemas legacy (ese script de Python que lleva 3 años corriendo en producción)
- No incluir APIs de terceros integradas en tu producto
- Subestimar el riesgo de sistemas "simples"

### Paso 2: Evaluación de Riesgo Detallada (Alto Riesgo)

**Duración estimada: 4-8 semanas (para sistemas de alto riesgo)**

Para cada sistema identificado como **alto riesgo**, necesitas una evaluación exhaustiva.

**Acciones concretas:**

1. **Análisis de impacto sobre derechos fundamentales**:
   - ¿El sistema puede discriminar por raza, género, edad, discapacidad?
   - ¿Afecta oportunidades de empleo, crédito, educación, servicios esenciales?
   - ¿Qué pasaría si falla? (Escenario del peor caso)

2. **Evaluación de sesgos en datos**:
   - ¿Tu dataset de entrenamiento es representativo de la población objetivo?
   - Ejemplo: Un sistema de RRHH entrenado solo con CVs de hombres discriminará a mujeres
   - Herramientas: Fairlearn (Microsoft), AI Fairness 360 (IBM), What-If Tool (Google)

3. **Pruebas de robustez**:
   - ¿Qué precisión tiene en diferentes subgrupos?
   - ¿Cómo maneja datos atípicos o adversarios?
   - ¿Se degrada con el tiempo (data drift)?

4. **Diseño de supervisión humana**:
   - ¿Quién puede intervenir en decisiones automatizadas?
   - ¿Cuándo se activa la revisión humana? (ej: cuando la confianza del modelo es <80%)
   - ¿Están formados los supervisores?

**Resultado esperado**: Un documento de evaluación de riesgos por cada sistema de alto riesgo, que incluya:
- Riesgos identificados (con severidad: baja, media, alta)
- Medidas de mitigación implementadas
- Procedimientos de monitoreo continuo
- Plan de respuesta ante incidentes

**Coste aproximado**:
- **PyME (1-2 sistemas de alto riesgo)**: €5.000-15.000 si lo haces con consultoría externa
- **Empresa mediana (3-10 sistemas)**: €20.000-60.000
- **Corporativo (10+ sistemas)**: €100.000+ (pero lo amortizas en evitar una multa millonaria)

### Paso 3: Documentación Técnica (Anexo IV)

**Duración estimada: 3-6 meses (paralelo con evaluación de riesgo)**

El Anexo IV del AI Act exige documentación técnica que pueda ser auditada. No basta con "lo sabemos internamente".

**Componentes obligatorios:**

1. **Descripción del sistema**:
   - Finalidad y contexto de uso
   - Usuarios previstos
   - Lógica de funcionamiento (explicado para no técnicos también)

2. **Datos de entrenamiento y testing**:
   - Origen (¿de dónde vienen los datos?)
   - Tamaño del dataset (ejemplos: 100K transacciones, 50K imágenes)
   - Período temporal cubierto
   - Proceso de limpieza y preprocesamiento
   - Sesgo detectado y medidas tomadas
   - División train/validation/test

3. **Arquitectura del modelo**:
   - Tipo de modelo (RandomForest, LSTM, Transformer, etc.)
   - Parámetros clave e hiperparámetros
   - Diagrama de flujo del pipeline

4. **Métricas de rendimiento**:
   - Precisión global (accuracy)
   - Precisión por subgrupo (por género, edad, etc.)
   - Recall, F1-score, AUC-ROC según caso de uso
   - Tasas de falsos positivos/negativos

5. **Gestión de riesgos**:
   - Riesgos residuales (aquellos que no se pueden eliminar)
   - Medidas de mitigación activas
   - Protocolo de actualización del sistema

6. **Supervisión humana**:
   - Roles y responsabilidades
   - Interfaces para supervisión
   - Procedimientos de escalado

7. **Ciberseguridad**:
   - Medidas contra ataques adversarios
   - Protección de datos sensibles
   - Plan de continuidad

**Herramientas útiles**:
- **Notion/Confluence**: Para documentación viva
- **GitHub**: Para versionar código y modelos
- **MLflow/Weights & Biases**: Para tracking de experimentos
- **DVC (Data Version Control)**: Para versionar datasets

**Resultado esperado**: Un paquete documental completo que puedas entregar a AESIA en caso de auditoría, sin sudar.

### Paso 4: Gobernanza y Responsabilidad

**Duración estimada: 2-3 meses**

El compliance no es un evento puntual. Es un **proceso continuo** que requiere gobernanza clara.

**Acciones concretas:**

1. **Designar un AI Compliance Officer**:
   - Puede ser el CTO, un Data Protection Officer ampliado, o un rol nuevo
   - Responsabilidades:
     - Mantener inventario de sistemas IA actualizado
     - Coordinar auditorías internas
     - Interlocutor con AESIA
     - Formación continua del equipo

2. **Establecer un comité de ética de IA** (para empresas >50 empleados):
   - Representación multidisciplinar: legal, técnico, negocio, RRHH
   - Reuniones trimestrales para revisar nuevos sistemas
   - Poder de veto sobre despliegues de alto riesgo

3. **Procedimiento de aprobación de nuevos sistemas**:
   - Todo sistema nuevo debe pasar por evaluación de riesgo **antes** de desarrollo
   - Template de evaluación rápida (10 preguntas clave)
   - Si es alto riesgo → aprobación del comité obligatoria

4. **Gestión de incidentes**:
   - ¿Qué haces si un sistema de IA toma una decisión discriminatoria?
   - Protocolo: detectar → pausar → investigar → remediar → reportar (a AESIA si es grave)
   - Timeframes claros (ej: pausa inmediata, reporte a autoridad en 72h)

5. **Auditorías internas periódicas**:
   - Mínimo anual para sistemas de alto riesgo
   - Revisión de logs, métricas, quejas de usuarios
   - Actualización de documentación

**Resultado esperado**: Una estructura organizativa que convierte el compliance en "business as usual", no en un proyecto de pánico cada vez que hay una auditoría.

### Paso 5: Transparencia y Derechos de Usuario

**Duración estimada: 1-2 meses**

El AI Act refuerza derechos que ya existían en GDPR, y añade otros nuevos.

**Acciones concretas:**

1. **Actualizar política de privacidad**:
   - Sección específica sobre uso de IA
   - Qué sistemas usas, para qué finalidad, qué datos procesan
   - Derechos del usuario (acceso, rectificación, oposición)

2. **Divulgación de IA en interfaces**:
   - Chatbots: mensaje al inicio ("Hola, soy un asistente de IA...")
   - Contenido sintético: marca de agua o texto ("Generado con IA")
   - Decisiones automatizadas: notificación al usuario ("Tu solicitud fue evaluada por un sistema automatizado. Puedes solicitar revisión humana.")

3. **Habilitar revisión humana**:
   - Si un usuario discrepa con una decisión automatizada (ej: rechazo de crédito), debe poder pedir que un humano revise el caso
   - Tiempo de respuesta razonable (ej: 5 días laborables)
   - Proceso documentado y accesible

4. **Explicabilidad**:
   - Usuarios afectados por decisiones de alto riesgo tienen derecho a entender por qué
   - No hace falta revelar el modelo completo, pero sí factores clave
   - Ejemplo: "Tu solicitud fue rechazada principalmente por: historial crediticio insuficiente, ingresos por debajo del umbral mínimo."

**Resultado esperado**: Interfaces y comunicaciones transparentes que empoderan a usuarios y demuestran buena fe regulatoria.

### Paso 6: Formación del Equipo

**Duración estimada: Continua**

El mejor sistema de compliance se cae si el equipo no entiende por qué existe.

**Acciones concretas:**

1. **Formación básica en AI Act para todos** (2 horas):
   - Qué es el AI Act, por qué importa
   - Obligaciones principales
   - Consecuencias del incumplimiento
   - A quién acudir si tienen dudas

2. **Formación técnica profunda para desarrolladores/data scientists** (1-2 días):
   - Cómo evaluar sesgos
   - Documentación técnica (Anexo IV)
   - Herramientas de fairness y robustness
   - Casos de estudio de incumplimiento

3. **Formación legal para compliance/legal** (1 día):
   - Detalles del Reglamento
   - Relación con GDPR
   - Gestión de auditorías
   - Respuesta a solicitudes de AESIA

4. **Talleres trimestrales de actualización**:
   - Nuevas guías de AESIA
   - Casos de sanción publicados
   - Lecciones aprendidas internas

**Coste aproximado**:
- **Formación externa**: €300-800/persona (cursos especializados)
- **Certificaciones** (ej: GAIPC®, ARTIBA): €1.500-3.000
- **Consultoría in-house**: €2.000-5.000/día para talleres personalizados

**Resultado esperado**: Un equipo que no solo cumple porque "hay que cumplir", sino porque entiende el valor de la IA responsable.

### Coste Total de Compliance: ¿Cuánto Presupuestar?

Los costes varían dramáticamente según tamaño y complejidad.

**Empresa pequeña (1-10 empleados, 1-2 sistemas de alto riesgo):**
- Consultoría inicial: €10.000-20.000
- Herramientas y formación: €5.000/año
- **Total primer año**: €15.000-25.000

**Empresa mediana (50-250 empleados, 3-10 sistemas de alto riesgo):**
- Consultoría y auditoría: €50.000-150.000
- Compliance Officer (coste interno): €50.000-80.000/año
- Herramientas y certificaciones: €15.000/año
- **Total primer año**: €115.000-245.000

**Gran empresa (250+ empleados, 10+ sistemas de alto riesgo):**
- Consultoría y auditoría externa: €200.000-500.000+
- Equipo de compliance interno (3-5 personas): €200.000-400.000/año
- Herramientas, certificaciones, formación: €50.000+/año
- **Total primer año**: €450.000-950.000+

**Pero recuerda**: Una sola multa del 3% de facturación puede superar todo esto. Para una empresa con €20M de ingresos, eso son **€600.000**. El compliance no es un gasto, es un seguro.

### Proveedores de Compliance en España

Si no tienes capacidad interna, estas son algunas consultorías especializadas en AI Act compliance:

**Grandes consultoras:**
- **Deloitte** (práctica de AI governance)
- **PwC** (AI assurance & ethics)
- **KPMG** (Responsible AI)
- **EY** (AI risk management)

**Especializadas:**
- **Sngular** (compliance técnico + implementación)
- **LexDoka** (legal AI + compliance legal)
- **OpenSistemas** (integración compliance en sistemas existentes)

**Herramientas SaaS de compliance:**
- **Credo AI** (AI governance platform)
- **Fiddler AI** (explicability & monitoring)
- **Arthur AI** (model monitoring & bias detection)
- **Holistic AI** (compliance automation)

### Sanciones Proporcionadas para PYMEs

El AI Act reconoce que una multa de €15M puede destruir una startup. Por eso incluye **proporcionalidad**:

- **Micro/pequeñas empresas** (< 50 empleados, < €10M facturación):
  - Multas reducidas (típicamente <€100.000 para primeras infracciones)
  - Acceso a sandbox regulatorio sin coste
  - Documentación simplificada

- **Medianas** (50-250 empleados):
  - Multas moduladas según capacidad financiera
  - Prioridad en programas de soporte de AESIA

El objetivo no es matar empresas, sino incentivar cumplimiento. Si actúas de buena fe, documentas tus esfuerzos, y respondes con transparencia ante AESIA, las sanciones serán proporcionales.

Pero si ignoras completamente el AI Act y operas un sistema de alto riesgo sin ninguna medida, ahí sí: las multas serán contundentes.

---

**La preparación para el AI Act no es opcional.** Pero tampoco tiene por qué ser paralizante.

Empieza hoy con el inventario. Identifica qué sistemas son realmente de alto riesgo (probablemente menos de los que crees). Prioriza. Y avanza paso a paso.

En 2027, cuando AESIA toque a tu puerta para una auditoría rutinaria, querrás poder responder con confianza: "Aquí está nuestra documentación completa, nuestro proceso de governance, y nuestros resultados de auditoría interna".

Esa tranquilidad se construye ahora, no cuando llegue la inspección.

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const newsCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    author: z.string().default('WorkLess AI Team'),
    category: z.enum(['openai', 'anthropic', 'google', 'meta', 'investigacion', 'industria', 'otros']),
    tags: z.array(z.string()),
    image: z.string().optional(),
    source: z.string().optional(),
    sourceUrl: z.string().url().optional(),
    featured: z.boolean().default(false),
  }),
});

const tutorialesCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/tutoriales' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    author: z.string().default('WorkLess AI Team'),
    difficulty: z.enum(['principiante', 'intermedio', 'avanzado']),
    duration: z.string(), // "30 minutos", "2 horas", etc.
    tags: z.array(z.string()),
    image: z.string().optional(),
    featured: z.boolean().default(false),
  }),
});

const herramientasCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/herramientas' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    author: z.string().default('WorkLess AI Team'),
    toolName: z.string(),
    toolUrl: z.string().url(),
    rating: z.number().min(1).max(5),
    pricing: z.enum(['gratis', 'freemium', 'pago', 'enterprise']),
    category: z.enum(['escritura', 'codigo', 'imagen', 'video', 'audio', 'productividad', 'otros']),
    pros: z.array(z.string()),
    cons: z.array(z.string()),
    affiliateLink: z.string().url().optional(),
    tags: z.array(z.string()),
    image: z.string().optional(),
    featured: z.boolean().default(false),
  }),
});

const casosDeUsoCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/casos-de-uso' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    author: z.string().default('WorkLess AI Team'),
    company: z.string(),
    industry: z.enum(['marketing', 'desarrollo', 'contenido', 'ventas', 'soporte', 'finanzas', 'otros']),
    roi: z.string().optional(), // "300% increase", "5 hours saved/week", etc.
    tags: z.array(z.string()),
    image: z.string().optional(),
    featured: z.boolean().default(false),
  }),
});

export const collections = {
  'news': newsCollection,
  'tutoriales': tutorialesCollection,
  'herramientas': herramientasCollection,
  'casos-de-uso': casosDeUsoCollection,
};

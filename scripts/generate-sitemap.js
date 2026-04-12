#!/usr/bin/env node
/**
 * Generate sitemap.xml for WorkLess.build
 * Run: node scripts/generate-sitemap.js
 */

import { writeFileSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const projectRoot = join(__dirname, '..');
const baseUrl = 'https://workless.build';

// Get all news articles
const newsDir = join(projectRoot, 'src/content/news');
const newsFiles = readdirSync(newsDir).filter(f => f.endsWith('.md'));

const staticPages = [
  { url: '/', priority: '1.0', changefreq: 'daily' },
  { url: '/news', priority: '0.9', changefreq: 'daily' },
  { url: '/herramientas-ia', priority: '0.9', changefreq: 'weekly' },
  { url: '/prompts', priority: '0.9', changefreq: 'weekly' },
  { url: '/calculadora-roi', priority: '0.8', changefreq: 'monthly' },
  { url: '/sobre', priority: '0.5', changefreq: 'monthly' },
];

// Generate news URLs from markdown files
const newsUrls = newsFiles.map(file => {
  const slug = file.replace('.md', '');
  return {
    url: `/news/${slug}`,
    priority: '0.8',
    changefreq: 'monthly',
  };
});

const allPages = [...staticPages, ...newsUrls];

// Build XML
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allPages.map(page => `  <url>
    <loc>${baseUrl}${page.url}</loc>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
  </url>`).join('\n')}
</urlset>`;

// Write to public/
const outputPath = join(projectRoot, 'public', 'sitemap.xml');
writeFileSync(outputPath, sitemap, 'utf-8');

console.log(`✅ Sitemap generated: ${outputPath}`);
console.log(`   Total URLs: ${allPages.length} (${staticPages.length} static + ${newsUrls.length} news)`);

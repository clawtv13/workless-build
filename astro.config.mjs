import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import react from '@astrojs/react';

export default defineConfig({
  site: 'https://workless.build',
  output: 'static',
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
    react(),
  ],
  build: {
    inlineStylesheets: 'auto',
    assets: 'assets',  // Avoid underscore prefix for GitHub Pages
  },
  vite: {
    build: {
      cssMinify: 'lightningcss',
    },
  },
});

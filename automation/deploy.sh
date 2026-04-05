#!/bin/bash
# Deploy to GitHub Pages

set -e

echo "🚀 Deploying WorkLess V2..."

cd "$(dirname "$0")/.."

# Build site
echo "📦 Building..."
npm run build

# Deploy to GitHub
echo "🔄 Pushing to GitHub..."
git add dist/
git commit -m "Deploy: $(date +'%Y-%m-%d %H:%M')" || echo "No changes"
git push origin main

echo "✅ Deployed!"
echo "🌐 Live at: https://workless.build"

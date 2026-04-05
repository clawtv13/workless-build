# 🚀 WorkLess V2 - Deployment Guide

## ✅ Status: FOUNDATION + AUTOMATION READY

**Completed:**
- ✅ Astro + Tailwind site
- ✅ Homepage + core pages
- ✅ Content collections configured
- ✅ RSS scraper (20 real news scraped!)
- ✅ Content generator (AI-powered)
- ✅ Database system
- ✅ Deployment scripts
- ✅ Cron automation ready

**Pending:**
- ⏳ Category page templates (agent working on it)
- ⏳ API keys configuration
- ⏳ GitHub repo setup
- ⏳ Initial content generation (with real keys)
- ⏳ Deploy to GitHub Pages

---

## 🔑 STEP 1: Configure API Keys

```bash
cd /root/.openclaw/workspace/workless-v2/automation
cp .env.example .env
nano .env
```

**Required:**
```
OPENAI_API_KEY=sk-...your-key...
```

**Optional (but recommended):**
```
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=your_github_token_here
```

---

## 📝 STEP 2: Generate Initial Content

**We have 20 news items scraped. Generate first 10 articles:**

```bash
cd /root/.openclaw/workspace/workless-v2/automation
source venv/bin/activate
python content_generator.py --limit=10
```

**This will:**
- ✅ Generate 10 Spanish articles from English sources
- ✅ Save to src/content/news/
- ✅ Mark as processed in database

**Time:** ~5-10 minutes (depends on API speed)

---

## 🏗️ STEP 3: Build Site

```bash
cd /root/.openclaw/workspace/workless-v2
npm run build
```

**Output:** `dist/` folder with static site

---

## 🌐 STEP 4: Deploy to GitHub Pages

### **Option A: GitHub repo + Pages (Recommended)**

```bash
cd /root/.openclaw/workspace/workless-v2

# Initialize repo
git init
git add .
git commit -m "Initial commit: WorkLess V2"

# Create GitHub repo (manual or CLI)
# Then:
git remote add origin https://github.com/yourusername/workless-build.git
git branch -M main
git push -u origin main

# Configure GitHub Pages:
# Settings → Pages → Source: GitHub Actions
# Create .github/workflows/deploy.yml (provided below)
```

### **Option B: Direct dist/ deploy**

```bash
cd /root/.openclaw/workspace/workless-v2/dist
git init
git add .
git commit -m "Deploy"
git push -f https://github.com/yourusername/workless-build.git main:gh-pages
```

---

## ⚙️ STEP 5: Setup Automation

**Install cron jobs:**

```bash
cd /root/.openclaw/workspace/workless-v2
bash automation/cron_setup.sh | crontab -
```

**This schedules:**
- Scraping every 2 hours
- Content generation 3x/day (08:00, 14:00, 20:00)
- Auto-deploy after generation
- Daily analytics

**Verify:**
```bash
crontab -l
```

---

## 📊 STEP 6: Monitor

**View logs:**
```bash
tail -f /root/.openclaw/workspace/workless-v2/automation/logs/*.log
```

**Check database:**
```bash
cd /root/.openclaw/workspace/workless-v2/automation
sqlite3 content.db "SELECT COUNT(*) FROM content_queue;"
sqlite3 content.db "SELECT COUNT(*) FROM content_queue WHERE published = 1;"
```

**Test pipeline manually:**
```bash
cd /root/.openclaw/workspace/workless-v2/automation
./venv/bin/python run_pipeline.py
```

---

## 🎯 Post-Launch Checklist

**Week 1:**
- [ ] Monitor cron jobs running
- [ ] Verify content quality
- [ ] Check Google Analytics
- [ ] Submit to Google Search Console
- [ ] Test all category pages

**Week 2:**
- [ ] Add AdSense
- [ ] Setup affiliate links
- [ ] Create newsletter signup backend
- [ ] Build analytics dashboard

**Month 1:**
- [ ] Optimize based on metrics
- [ ] A/B test headlines
- [ ] Expand content sources
- [ ] Add more automation

---

## 📈 Success Metrics

**Target Month 1:**
- 100+ posts auto-generated
- 10K+ pageviews
- 200+ email subscribers
- $100-300 revenue

**Track in Google Analytics:**
- Traffic sources
- Top performing posts
- Bounce rate
- Time on page
- Conversion rates

---

## 🆘 Troubleshooting

**Build fails:**
```bash
cd /root/.openclaw/workspace/workless-v2
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
npm run build
```

**No content generating:**
```bash
# Check API key set
cd automation
cat .env | grep OPENAI

# Test manually
./venv/bin/python content_generator.py --limit=1
```

**Cron not running:**
```bash
# Check cron service
systemctl status cron

# View cron logs
grep CRON /var/log/syslog | tail -20
```

---

**Built with OpenClaw by n0mad - April 5, 2026**

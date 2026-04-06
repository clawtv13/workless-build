# WorkLess.build Automation System

## 🎯 Overview

Fully automated content pipeline:
- Scrapes AI news every 2 hours
- Auto-researches tutorials, tools, use cases
- Scores content (0-50)
- Generates Spanish articles
- Quality review (humanize, structure, grammar)
- Auto-publishes 4-5 posts/day (08:00, 12:00, 16:00, 20:00 UTC)
- Telegram notifications per post

---

## ✅ Status: COMPLETE & READY

**Built:** April 5, 2026  
**Location:** `/root/.openclaw/workspace/workless-v2/automation/`

---

## 🔧 Components

### **1. database.py**
- SQLite schema
- Add/get/mark functions
- Deduplication by URL

### **2. sources/rss_scraper.py**
- 6 RSS feeds (OpenAI, Anthropic, Google, DeepMind, HF, Stability)
- Runs every 2 hours
- Adds to queue

### **3. auto_researcher.py**
- Finds trending tools (Product Hunt, HN)
- Tutorial gaps (SEO research)
- Company case studies
- Runs daily 06:00 UTC

### **4. scorer.py**
- 5-factor scoring (0-50):
  - Impact (0-10)
  - Spanish relevance (0-10)
  - Actionability (0-10)
  - Timeliness (0-10)
  - Differentiation (0-10)
- Runs daily 07:00 UTC
- Filter: 25+ passes

### **5. content_generator.py**
- Generates Spanish articles (400-600 words)
- Professional, accessible, no hype
- Uses OpenClaw/OpenRouter

### **6. quality_reviewer.py**
- Removes AI patterns
- Checks structure
- Humanizes text
- Scores quality (0-10)
- Approval gate: 8+ auto-publish, 6-7 notify, <6 skip

### **7. telegram_notifier.py**
- Per-post notifications
- Format: "✅ Published: [title] - [URL]"
- Chat ID: 8116230130

### **8. publisher.py**
- npm run build
- Deploy to gh-pages
- Trigger Telegram notification

### **9. master_cron.py**
- Orchestrates full pipeline
- Runs 4x/day (08:00, 12:00, 16:00, 20:00)
- Category mix: 50% news, 25% tutorials, 25% reviews/casos
- Generates 1 post per run (4/day)

### **10. cron_setup.sh**
- Install all cron jobs
- View/manage automation

---

## 🚀 Quick Start

### **1. Configure .env**
```bash
cd /root/.openclaw/workspace/workless-v2/automation
nano .env
```

Required:
```
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
GITHUB_TOKEN=your_token
GITHUB_REPO=user/repo
```

### **2. Install cron jobs**
```bash
bash cron_setup.sh | crontab -
```

### **3. Verify**
```bash
crontab -l
```

---

## 📊 Monitoring

**View logs:**
```bash
tail -f logs/*.log
```

**Check database:**
```bash
sqlite3 content.db "SELECT COUNT(*), type FROM content_queue GROUP BY type;"
sqlite3 content.db "SELECT COUNT(*) FROM content_queue WHERE published = 1;"
```

**Test components:**
```bash
# Test scraping
./venv/bin/python sources/rss_scraper.py

# Test scoring
./venv/bin/python scorer.py

# Test one full cycle
./venv/bin/python master_cron.py
```

---

## ⏰ Schedule

**Daily:**
- `06:00` - Auto-research (find tutorials/tools/casos)
- `07:00` - Score new items
- `08:00` - Post 1 (News)
- `12:00` - Post 2 (Tutorial)
- `16:00` - Post 3 (Review/Caso)
- `20:00` - Post 4 (News)

**Every 2 hours:**
- RSS scraping

**Target:** 4-5 posts/day, fully automated

---

## 🔒 Security

- `.env` file in `.gitignore` (never committed)
- GitHub token in environment only
- Telegram token protected
- Database local only

---

## 🎯 Success Metrics

**Week 1:**
- 28-35 posts auto-generated
- 0 manual intervention
- 4-5 Telegram notifications/day

**Month 1:**
- 120-150 posts
- All 4 categories balanced
- SEO indexing started

---

**Built with OpenClaw by n0mad - April 5, 2026**

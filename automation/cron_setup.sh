#!/bin/bash
# Setup cron jobs for WorkLess.build automation

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "📋 To install these cron jobs:"
    echo "   bash /root/.openclaw/workspace/workless-v2/automation/cron_setup.sh | crontab -"
    echo ""
    echo "📊 To view current crontab:"
    echo "   crontab -l"
    echo ""
    echo "🗑️  To remove all WorkLess cron jobs:"
    echo "   crontab -r"
    echo ""
    echo "📈 To view logs:"
    echo "   tail -f /root/.openclaw/workspace/workless-v2/automation/logs/*.log"
    exit 0
fi

# Output crontab entries only (no extra text)
cat << 'EOF'
# ============================================================
# WorkLess.build Automation Cron Jobs
# ============================================================

# RSS Scraping - Every 2 hours
0 */2 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python sources/rss_scraper.py >> logs/scraper.log 2>&1

# Auto-research - Daily at 06:00 UTC (find tutorials/reviews/casos)
0 6 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python auto_researcher.py >> logs/researcher.log 2>&1

# Scoring - Daily at 07:00 UTC (score new items)
0 7 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python scorer.py >> logs/scorer.log 2>&1

# Master Cron - 4x per day (08:00, 12:00, 16:00, 20:00 UTC)
# Generates + reviews + publishes 1 post per run
0 8 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python master_cron.py >> logs/master.log 2>&1
0 12 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python master_cron.py >> logs/master.log 2>&1
0 16 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python master_cron.py >> logs/master.log 2>&1
0 20 * * * cd /root/.openclaw/workspace/workless-v2/automation && ./venv/bin/python master_cron.py >> logs/master.log 2>&1
EOF

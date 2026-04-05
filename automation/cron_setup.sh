#!/bin/bash
# Setup cron jobs for automation

WORKDIR="/root/.openclaw/workspace/workless-v2/automation"

cat << EOF
# WorkLess AI Automation Cron Jobs
# Add these to your crontab with: crontab -e

# Scrape sources every 2 hours
0 */2 * * * cd $WORKDIR && ./venv/bin/python sources/rss_scraper.py >> logs/scraper.log 2>&1

# Generate content 3x per day (08:00, 14:00, 20:00 UTC)
0 8,14,20 * * * cd $WORKDIR && ./venv/bin/python content_generator.py --limit=5 >> logs/generator.log 2>&1

# Build and deploy after generation (30 min later)
30 8,14,20 * * * cd $WORKDIR && ./deploy.sh >> logs/deploy.log 2>&1

# Daily analytics at midnight
0 0 * * * cd $WORKDIR && ./venv/bin/python analytics.py >> logs/analytics.log 2>&1

EOF

echo ""
echo "📋 To install:"
echo "   bash automation/cron_setup.sh | crontab -"
echo ""
echo "📊 To view logs:"
echo "   tail -f automation/logs/*.log"

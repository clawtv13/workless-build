#!/bin/bash
# OpenClaw agent script - processes generation requests from Python automation
# Called by heartbeat or dedicated cron

QUEUE_DIR="/tmp/workless-generation"
REQUEST_FILE="$QUEUE_DIR/request.json"
RESPONSE_FILE="$QUEUE_DIR/response.md"
LOCK_FILE="$QUEUE_DIR/lock"

# Check if request exists
if [ ! -f "$REQUEST_FILE" ]; then
    exit 0  # No request pending
fi

# Check if lock exists (request is active)
if [ ! -f "$LOCK_FILE" ]; then
    exit 0  # Request already processed
fi

# Parse request
TITLE=$(jq -r '.title' "$REQUEST_FILE")
SUMMARY=$(jq -r '.summary' "$REQUEST_FILE")
SOURCE=$(jq -r '.source' "$REQUEST_FILE")

echo "📝 Processing generation request: $TITLE"

# This is a marker - the actual generation will be done by OpenClaw agent
# when it reads this file during heartbeat checks

# Signal that agent is working on it
echo "AGENT_PROCESSING" > "$LOCK_FILE.processing"

exit 0

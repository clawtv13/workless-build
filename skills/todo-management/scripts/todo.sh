#!/bin/bash
# Simple todo management for agent-autopilot
# Usage: todo.sh entry list|create|status

DB_FILE="${DB_FILE:-./todo.db}"

init_db() {
    if [ ! -f "$DB_FILE" ]; then
        sqlite3 "$DB_FILE" <<EOF
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    priority INTEGER DEFAULT 5,
    group_name TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
EOF
    fi
}

case "$1" in
    entry)
        case "$2" in
            list)
                init_db
                sqlite3 "$DB_FILE" "SELECT id, status, priority, title, group_name FROM entries ORDER BY priority DESC, created_at ASC;" | column -t -s "|"
                ;;
            create)
                init_db
                TITLE="$3"
                GROUP=""
                PRIORITY=5
                
                shift 3
                while [[ $# -gt 0 ]]; do
                    case "$1" in
                        --group=*) GROUP="${1#*=}"; shift ;;
                        --priority=*) PRIORITY="${1#*=}"; shift ;;
                        *) shift ;;
                    esac
                done
                
                sqlite3 "$DB_FILE" "INSERT INTO entries (title, group_name, priority) VALUES ('$TITLE', '$GROUP', $PRIORITY);"
                echo "✅ Created: $TITLE"
                ;;
            status)
                init_db
                ID="$3"
                shift 3
                while [[ $# -gt 0 ]]; do
                    case "$1" in
                        --status=*) STATUS="${1#*=}"; shift ;;
                        *) shift ;;
                    esac
                done
                
                sqlite3 "$DB_FILE" "UPDATE entries SET status='$STATUS', updated_at=CURRENT_TIMESTAMP WHERE id=$ID;"
                echo "✅ Updated entry $ID to $STATUS"
                ;;
            *)
                echo "Usage: todo.sh entry [list|create|status]"
                exit 1
                ;;
        esac
        ;;
    *)
        echo "Usage: todo.sh entry [command]"
        exit 1
        ;;
esac

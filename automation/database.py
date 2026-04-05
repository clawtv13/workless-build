import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "content.db"

def init_database():
    """Initialize SQLite database with schema"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS content_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            type TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT UNIQUE NOT NULL,
            summary TEXT,
            raw_content TEXT,
            discovered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            processed BOOLEAN DEFAULT 0,
            published BOOLEAN DEFAULT 0,
            metadata TEXT
        )
    ''')
    
    c.execute('''
        CREATE INDEX IF NOT EXISTS idx_processed ON content_queue(processed)
    ''')
    
    c.execute('''
        CREATE INDEX IF NOT EXISTS idx_type ON content_queue(type)
    ''')
    
    conn.commit()
    conn.close()
    print(f"✓ Database initialized at {DB_PATH}")

def add_to_queue(source, content_type, title, url, summary="", raw_content="", metadata=""):
    """Add content to queue (with deduplication)"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    try:
        c.execute('''
            INSERT INTO content_queue (source, type, title, url, summary, raw_content, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (source, content_type, title, url, summary, raw_content, metadata))
        conn.commit()
        return c.lastrowid
    except sqlite3.IntegrityError:
        # URL already exists
        return None
    finally:
        conn.close()

def get_unprocessed(limit=10):
    """Get unprocessed items"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''
        SELECT id, source, type, title, url, summary, raw_content, metadata
        FROM content_queue
        WHERE processed = 0
        ORDER BY discovered_at DESC
        LIMIT ?
    ''', (limit,))
    
    rows = c.fetchall()
    conn.close()
    
    return [dict(zip(['id', 'source', 'type', 'title', 'url', 'summary', 'raw_content', 'metadata'], row)) for row in rows]

def mark_processed(item_id):
    """Mark item as processed"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE content_queue SET processed = 1 WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

def mark_published(item_id):
    """Mark item as published"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE content_queue SET published = 1 WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()

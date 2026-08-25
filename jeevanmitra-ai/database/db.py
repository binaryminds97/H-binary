"""
Minimal SQLite helper for Phase 1.
Implements a simple function to get a DB connection. No migrations or heavy logic yet.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'data' / 'jeevanmitra.db'

def get_conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    print('DB path:', DB_PATH)

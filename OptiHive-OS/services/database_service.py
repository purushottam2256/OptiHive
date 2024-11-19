import sqlite3

DB_FILE = "battery_data.db"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS battery_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT,
            charge_remaining INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def log_battery_data(name, status, charge_remaining):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO battery_logs (name, status, charge_remaining)
        VALUES (?, ?, ?)
    """, (name, status, charge_remaining))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    log_battery_data("Battery1", "Discharging", 85)

import sqlite3

DB_NAME = "jobs.db"

def create_table():
    """Create a table to store job listings if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            job_url TEXT,
            date_posted TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_job(job):
    """Insert a job listing into the database (ignores duplicates)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO jobs (id, title, company, location, job_url, date_posted)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (job["id"], job["title"], job["company"], job["location"], job["job_url"], job["date_posted"]))

    conn.commit()
    conn.close()

def job_exists(job_id):
    """Check if a job already exists in the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM jobs WHERE id = ?", (job_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None

# Run this file to create the table initially
if __name__ == "__main__":
    create_table()
    print("✅ Database and table are ready!")

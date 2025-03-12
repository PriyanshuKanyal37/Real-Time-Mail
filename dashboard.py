import streamlit as st
import sqlite3
from database import job_exists, insert_job
from email_sender import send_email

# Connect to SQLite database
DB_NAME = "jobs.db"

def get_all_jobs():
    """Fetch all jobs from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, location, job_url FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return jobs

# Streamlit Dashboard
st.set_page_config(page_title="Job Tracker", layout="wide")

st.title("📩 Real-Time Job Tracker & Email Sender")

# Fetch jobs from the database
jobs = get_all_jobs()

# Display jobs in a table
if jobs:
    st.write("### Stored Job Listings")
    for job in jobs:
        job_id, title, company, location, job_url = job
        st.write(f"**{title}** at **{company}** ({location})")
        st.markdown(f"[🔗 Apply Here]({job_url})")

        # Email sending button
        if st.button(f"✉ Send Email for {title}", key=job_id):
            subject = f"Application for {title} at {company}"
            body = f"""
            Hello Hiring Manager,<br><br>
            I came across the {title} position at {company} and I am very interested.<br>
            I have experience in this domain, and I believe I would be a great fit for your team.<br><br>
            Here is my profile for your reference.<br>
            <a href="{job_url}">View Job Posting</a><br><br>
            Looking forward to your response.<br><br>
            Best Regards,<br>
            Priyanshu Kanyal
            """
            send_email("recruiter@example.com", subject, body)
            st.success(f"✅ Email Sent for {title} at {company}")
else:
    st.write("⚠ No jobs found in the database.")


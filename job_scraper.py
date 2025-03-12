import requests
from config import JSEARCH_API_KEY  # Import API Key from config
from database import insert_job, job_exists  # Import database functions
from email_sender import send_email  # Import email sending function

JOBS_API_URL = "https://jobs-search-api.p.rapidapi.com/getjobs"

HEADERS = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "jobs-search-api.p.rapidapi.com",
    "x-rapidapi-key": JSEARCH_API_KEY
}

def fetch_jobs(search_term="Cloud Engineer", location="New York", num_results=5):
    """Fetch jobs from multiple job sites like Indeed, LinkedIn, Glassdoor."""
    payload = {
        "search_term": search_term,
        "location": location,
        "results_wanted": num_results,
        "site_name": ["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        "distance": 50,
        "job_type": "fulltime",
        "is_remote": False,
        "linkedin_fetch_description": False,
        "hours_old": 72
    }

    response = requests.post(JOBS_API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        jobs = data.get("jobs", [])

        for job in jobs:
            job_id = job["id"]
            if not job_exists(job_id):  # Only send emails for new jobs
                insert_job(job)  # Save job in database

                # Generate email content
                subject = f"Application for {job['title']} at {job['company']}"
                body = f"""
                Hello Hiring Manager,<br><br>
                I came across the {job['title']} position at {job['company']} and I am very interested.<br>
                I have experience in this domain, and I believe I would be a great fit for your team.<br><br>
                Here is my profile for your reference.<br>
                <a href="{job['job_url']}">View Job Posting</a><br><br>
                Looking forward to your response.<br><br>
                Best Regards,<br>
                Priyanshu Kanyal
                """

                # Send email
                send_email("recruiter@example.com", subject, body)

                print(f"✅ Email Sent for: {job['title']} at {job['company']}")

        return jobs
    else:
        print(f"Error fetching jobs: {response.status_code}, {response.text}")
        return []

# Test function
if __name__ == "__main__":
    fetch_jobs("Cloud Engineer", "New York", 5)

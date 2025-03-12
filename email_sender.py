import sib_api_v3_sdk
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
BREVO_API_KEY = os.getenv("EMAIL_API_KEY")

def send_email(recipient_email, subject, body):
    """Send an email using Brevo API."""
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key["api-key"] = BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    sender = {"name": "Priyanshu Kanyal", "email": "your_email@example.com"}
    to = [{"email": recipient_email, "name": "Hiring Manager"}]

    email_data = {
        "sender": sender,
        "to": to,
        "subject": subject,
        "htmlContent": f"<html><body><p>{body}</p></body></html>"
    }

    try:
        api_instance.send_transac_email(email_data)
        print(f"✅ Email sent to {recipient_email}")
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")

# Test sending an email
if __name__ == "__main__":
    send_email("test@example.com", "Test Job Application", "Hello, I am interested in this role.")

import threading
import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY


def send_email_async(email_msg):
    """
    Send email in a separate thread using Resend API.
    """

    def task():
        try:
            resend.Emails.send(
                {
                    "from": "onboarding@resend.dev",
                    "to": list(email_msg.to),
                    "subject": email_msg.subject,
                    "text": email_msg.body,
                }
            )
        except Exception as e:
            print(f"Failed to send email: {e}")

    threading.Thread(target=task, daemon=True).start()

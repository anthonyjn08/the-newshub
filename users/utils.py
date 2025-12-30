import threading
from resend import Resend
from django.conf import settings

resend_client = Resend(api_key=settings.RESEND_API_KEY)


def send_email_async(email_msg):
    """
    Send email in a separate thread using Resend API.
    """

    def task():
        resend_client.emails.send(
            from_email=email_msg.from_email,
            to=email_msg.to,
            subject=email_msg.subject,
            text=email_msg.body,
        )

    threading.Thread(target=task).start()

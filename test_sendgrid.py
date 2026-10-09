import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

print("FROM:", os.getenv("FROM_EMAIL"))
print("TO:", os.getenv("TO_EMAIL"))

api_key = os.getenv("SENDGRID_API_KEY")

if not api_key:
    print("❌ SENDGRID_API_KEY not found")
    exit()

print("✅ API key found")

message = Mail(
    from_email=os.getenv("FROM_EMAIL"),
    to_emails=os.getenv("TO_EMAIL"),
    subject="AI Travel Agent - Test Email",
    html_content="""
    <html>
        <body>
            <h2>Test Email</h2>
            <p>This is a test email from my AI Travel Agent.</p>
        </body>
    </html>
    """
)

try:
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)

    print("Status Code:", response.status_code)
    print("Response Body:", response.body)

    if response.status_code == 202:
        print("✅ SUCCESS - SendGrid accepted the email!")
    else:
        print("❌ SendGrid rejected the email.")

except Exception as e:
    print("❌ ERROR:", repr(e))

    if hasattr(e, "body"):
        print("Error body:", e.body)

    if hasattr(e, "status_code"):
        print("Status code:", e.status_code)
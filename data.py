# data.py
# 20 prebuilt email scenarios (single difficulty).
# Each item includes: subject, from_name, from_email, to, body, is_phish, indicators, explanation.

EMAILS = [
    {
        "id": 1,
        "subject": "Action Required: Password Expiration Notice",
        "from_name": "IT Helpdesk",
        "from_email": "it-support@company-secure.com",
        "to": "you@company.com",
        "body": (
            "Your password expires in 2 hours.\n\n"
            "To avoid losing access, verify your account now:\n"
            "http://company-secure.com.verify-login[.]ru/reset\n\n"
            "Failure to act will lock your account."
        ),
        "is_phish": True,
        "indicators": [
            "Urgency/threat (\"2 hours\", \"lock your account\")",
            "Suspicious link domain/subdomain mismatch (.ru, verify-login)",
            "Asks to 'verify' via link instead of normal IT process",
        ],
        "explanation": "Real IT notices typically link to internal portals and won’t use odd external domains or threats."
    },
    {
        "id": 2,
        "subject": "Invoice #10483 Attached",
        "from_name": "Accounts Payable",
        "from_email": "ap@vendor-payments.com",
        "to": "you@company.com",
        "body": (
            "Hi,\n\nPlease see the attached invoice #10483 for processing.\n"
            "If you have questions, reply to this email.\n\nThanks,\nAP Team"
        ),
        "is_phish": False,
        "indicators": [
            "No link; asks to reply if questions",
            "Reasonable tone, no urgency",
        ],
        "explanation": "Benign-looking invoices can still be risky, but this one lacks typical phishing pressure and suspicious links."
    },
    {
        "id": 3,
        "subject": "Unusual Sign-in Activity Detected",
        "from_name": "Microsoft Account Team",
        "from_email": "no-reply@micros0ft-security.com",
        "to": "you@company.com",
        "body": (
            "We detected unusual sign-in activity.\n\n"
            "Review activity here:\n"
            "https://micros0ft-security.com/activity\n\n"
            "If this wasn't you, secure your account immediately."
        ),
        "is_phish": True,
        "indicators": [
            "Lookalike domain (micros0ft with zero)",
            "Pushes you to click link",
        ],
        "explanation": "Legit Microsoft domains are microsoft.com; attackers use lookalikes to steal credentials."
    },
    {
        "id": 4,
        "subject": "Meeting notes from today",
        "from_name": "Jordan (Project Lead)",
        "from_email": "jordan@company.com",
        "to": "you@company.com",
        "body": (
            "Thanks for jumping on earlier.\n"
            "Here are the notes and action items:\n"
            "- Update ticket categories\n"
            "- Confirm rollout date\n\n"
            "Let me know if I missed anything."
        ),
        "is_phish": False,
        "indicators": [
            "Internal sender domain",
            "No links/attachments",
            "Specific context",
        ],
        "explanation": "Contextual, internal messages with no clickbait are usually legit."
    },
    {
        "id": 5,
        "subject": "Your package is on hold: confirm delivery details",
        "from_name": "FedEx Support",
        "from_email": "support@fedex-shipping-alerts.com",
        "to": "you@company.com",
        "body": (
            "We couldn't deliver your package.\n\n"
            "Confirm delivery address:\n"
            "http://fedex-shipping-alerts.com/confirm\n\n"
            "A re-delivery fee may apply."
        ),
        "is_phish": True,
        "indicators": [
            "Brand mismatch domain (not fedex.com)",
            "HTTP (not HTTPS)",
            "Pressure via fee",
        ],
        "explanation": "Shipping scams commonly use brand names with non-official domains."
    },
    {
        "id": 6,
        "subject": "VPN Maintenance Tonight",
        "from_name": "Network Operations",
        "from_email": "netops@company.com",
        "to": "you@company.com",
        "body": (
            "Heads up: VPN maintenance tonight 11 PM–1 AM CST.\n"
            "Expect brief disconnects. No action required.\n\n"
            "If you experience issues tomorrow, open a ticket."
        ),
        "is_phish": False,
        "indicators": [
            "No action requested",
            "Internal sender",
            "Clear window and instructions",
        ],
        "explanation": "Legit maintenance notices typically say 'no action required' and route problems to normal support channels."
    },
    {
        "id": 7,
        "subject": "DocuSign: Please review document",
        "from_name": "DocuSign",
        "from_email": "docusign@docusign-secure.com",
        "to": "you@company.com",
        "body": (
            "You have received a document to review.\n\n"
            "Review now:\n"
            "https://docusign-secure.com/review/8d92\n\n"
            "Document expires in 24 hours."
        ),
        "is_phish": True,
        "indicators": [
            "Non-official domain (not docusign.com)",
            "Urgency (expires soon)",
        ],
        "explanation": "Real DocuSign links should resolve to official domains; attackers mimic signing workflows."
    },
    {
        "id": 8,
        "subject": "Updated PTO Policy (FY2026)",
        "from_name": "HR Team",
        "from_email": "hr@company.com",
        "to": "you@company.com",
        "body": (
            "We updated the PTO policy effective FY2026.\n"
            "Please review on the intranet under HR Policies.\n\n"
            "No action required unless you have questions."
        ),
        "is_phish": False,
        "indicators": [
            "Refers to intranet rather than external link",
            "No urgency",
            "Internal sender",
        ],
        "explanation": "References internal resources without external links—lower risk."
    },
    {
        "id": 9,
        "subject": "Payment failed — update billing to avoid service interruption",
        "from_name": "Streaming Billing",
        "from_email": "billing@streaming-support.com",
        "to": "you@company.com",
        "body": (
            "Your last payment failed.\n\n"
            "Update billing now:\n"
            "http://streaming-support.com/billing\n\n"
            "Service interruption may occur."
        ),
        "is_phish": True,
        "indicators": [
            "Generic service name",
            "HTTP link",
            "Threat of interruption",
        ],
        "explanation": "Billing scams push urgency and links; verify through known official app/site instead."
    },
    {
        "id": 10,
        "subject": "Shared file: 'Q2_Budget.xlsx'",
        "from_name": "SharePoint",
        "from_email": "no-reply@sharepoint-files.com",
        "to": "you@company.com",
        "body": (
            "A file has been shared with you: Q2_Budget.xlsx\n\n"
            "Open file:\n"
            "https://sharepoint-files.com/open?id=1029\n"
        ),
        "is_phish": True,
        "indicators": [
            "Non-official SharePoint domain",
            "Unexpected file share",
        ],
        "explanation": "SharePoint/Drive phishing often uses fake 'shared file' pages to steal credentials."
    },
    {
        "id": 11,
        "subject": "Ticket Update: VPN Access Request #38421",
        "from_name": "Service Desk",
        "from_email": "servicedesk@company.com",
        "to": "you@company.com",
        "body": (
            "Your request #38421 has been updated.\n"
            "Status: Approved\n\n"
            "Next steps: You will receive setup instructions separately."
        ),
        "is_phish": False,
        "indicators": [
            "Internal sender",
            "Specific ticket number",
            "No link asking for credentials",
        ],
        "explanation": "Specific internal context with no credential-harvesting link is usually legit."
    },
    {
        "id": 12,
        "subject": "URGENT: Payroll direct deposit needs verification",
        "from_name": "Payroll",
        "from_email": "payroll@company-payroll.com",
        "to": "you@company.com",
        "body": (
            "We detected an issue with your direct deposit.\n"
            "Verify within 1 hour to prevent delay:\n"
            "https://company-payroll.com.verify-now[.]top/login\n"
        ),
        "is_phish": True,
        "indicators": [
            "Urgency (1 hour)",
            "Suspicious TLD (.top) and subdomain tricks",
            "Asks to verify via link",
        ],
        "explanation": "Payroll phishing is common; always use HR portal via known URL."
    },
    {
        "id": 13,
        "subject": "Security training reminder",
        "from_name": "Learning Platform",
        "from_email": "training@company.com",
        "to": "you@company.com",
        "body": (
            "Reminder: complete annual security training by Friday.\n"
            "Access via the LMS from the intranet.\n\n"
            "Thanks."
        ),
        "is_phish": False,
        "indicators": [
            "Internal sender",
            "Points to intranet/LMS",
        ],
        "explanation": "Training reminders typically route you to internal platforms rather than external links."
    },
    {
        "id": 14,
        "subject": "Google: Suspicious login blocked",
        "from_name": "Google Security",
        "from_email": "no-reply@googIe.com",
        "to": "you@company.com",
        "body": (
            "We blocked a suspicious sign-in attempt.\n"
            "Confirm your identity:\n"
            "https://accounts.googIe.com/secure\n"
        ),
        "is_phish": True,
        "indicators": [
            "Lookalike domain: googIe (capital i) instead of google",
            "Asks to confirm via link",
        ],
        "explanation": "Attackers use character lookalikes to create fake domains that appear legit at a glance."
    },
    {
        "id": 15,
        "subject": "Re: Quick question",
        "from_name": "CEO Office",
        "from_email": "ceo.office@company-executive.com",
        "to": "you@company.com",
        "body": (
            "Are you available? I need you to purchase gift cards ASAP.\n"
            "Reply with your personal number."
        ),
        "is_phish": True,
        "indicators": [
            "Gift card scam pattern",
            "Urgency and unusual request",
            "External-ish domain for 'CEO office'",
        ],
        "explanation": "Classic impersonation scam: urgency + gift cards + moving convo off official channels."
    },
    {
        "id": 16,
        "subject": "Lunch order for Friday",
        "from_name": "Team Coordinator",
        "from_email": "coordinator@company.com",
        "to": "you@company.com",
        "body": (
            "We’re ordering lunch for Friday.\n"
            "Reply with your choice by 3 PM."
        ),
        "is_phish": False,
        "indicators": [
            "Low stakes, internal sender",
            "No link or credential request",
        ],
        "explanation": "Normal internal coordination message."
    },
    {
        "id": 17,
        "subject": "Dropbox: Your storage is full",
        "from_name": "Dropbox",
        "from_email": "no-reply@dropbox-alerts.net",
        "to": "you@company.com",
        "body": (
            "Your Dropbox storage is full.\n"
            "Upgrade now to avoid file sync errors:\n"
            "http://dropbox-alerts.net/upgrade"
        ),
        "is_phish": True,
        "indicators": [
            "Non-official domain",
            "HTTP link",
            "Pressure to upgrade",
        ],
        "explanation": "Legit services usually use official domains and HTTPS; verify via the app or official site."
    },
    {
        "id": 18,
        "subject": "New device enrolled",
        "from_name": "IT Security",
        "from_email": "security@company.com",
        "to": "you@company.com",
        "body": (
            "A new device was enrolled in MDM for your account.\n"
            "If this was not you, contact the Service Desk.\n"
            "No action required through email."
        ),
        "is_phish": False,
        "indicators": [
            "No action via email",
            "Internal sender",
            "Directs to Service Desk",
        ],
        "explanation": "Good security notifications don’t ask for passwords; they route you to official support."
    },
    {
        "id": 19,
        "subject": "Bank Alert: Verify recent transaction",
        "from_name": "Bank Alerts",
        "from_email": "alerts@banking-secure.co",
        "to": "you@company.com",
        "body": (
            "We noticed a transaction of $1,250.\n"
            "Verify now:\n"
            "https://banking-secure.co/login\n"
        ),
        "is_phish": True,
        "indicators": [
            "Generic 'bank alerts' sender",
            "Suspicious domain (not your bank)",
            "Urgency and link to login",
        ],
        "explanation": "Financial phishing pushes fear; verify by calling the bank or using the official app."
    },
    {
        "id": 20,
        "subject": "Team access granted: Shared Drive",
        "from_name": "IT Automation",
        "from_email": "it-automation@company.com",
        "to": "you@company.com",
        "body": (
            "Access granted: Shared Drive 'IT-Projects'.\n"
            "If you did not request this, open a ticket with Service Desk."
        ),
        "is_phish": False,
        "indicators": [
            "Internal sender",
            "No external links",
            "Directs to ticketing",
        ],
        "explanation": "Legit access notifications often include official follow-up paths (ticketing)."
    },
]

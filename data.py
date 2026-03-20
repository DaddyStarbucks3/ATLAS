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
       "explanation": "Real IT notices typically link to internal portals and won1 AM CST.\n"
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
       "explanation": "References internal resources without external links update billing to avoid service interruption",
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
           "Wet ask for passwords; they route you to official support."
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

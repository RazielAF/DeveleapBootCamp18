import re

def main(txt):
   
    email_pattern = r'\b[\w.]+@[\w.]+\b'
    found_emails = re.findall(email_pattern, txt)

    
    unique_emails = {}

    for email in found_emails:
        lower_case_email = email.lower()
        if lower_case_email not in unique_emails:
            unique_emails[lower_case_email] = email

    sorted_emails = sorted(unique_emails.values(), key=lambda x: (x.split('@')[1], x.split('@')[0]))

    return sorted_emails
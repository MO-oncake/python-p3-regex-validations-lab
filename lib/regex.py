import re

# Regex for names: allows letters, spaces (only single space allowed), hyphens, and apostrophes, must start with an uppercase letter
name = r"^(?!.*  )[A-Z][a-zA-Z' -]+$"
name_regex = re.compile(name)

# Regex for phone numbers: supports formats like 5555555555, 555-555-5555, (555) 555-5555
phone_number = r"^(?:\(\d{3}\)\s?|\d{3}[-]?)(\d{3})[-]?(\d{4})$"
phone_regex = re.compile(phone_number)

# Regex for email addresses: follows common patterns for valid emails
email_address = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
import re

log = "arn:aws:kms:us-east-1:752442278108:key"
pattern = r'key/([0-9a-fA-F\-]+)'

match = re.search(pattern, log)
if match:
    key_id = match.group(1)
    print("Extracted Key ID:", key_id)
else:
    print("Key ID not found in the log.")

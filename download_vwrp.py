import requests
import os
import datetime
import subprocess

# Vanguard VWRP holdings URL (Example, replace with the actual one)
VWRP_HOLDINGS_URL = "https://www.vanguard.co.uk/content/dam/intl/europe/documents/en/VWRP_holdings.csv"

# Define folder and filename
SAVE_DIR = "vwrp_holdings"
DATE_STR = datetime.datetime.now().strftime("%Y-%m-%d")
FILENAME = f"VWRP_holdings_{DATE_STR}.csv"

# Ensure save directory exists
os.makedirs(SAVE_DIR, exist_ok=True)
FILE_PATH = os.path.join(SAVE_DIR, FILENAME)

# Download the file
response = requests.get(VWRP_HOLDINGS_URL)
if response.status_code == 200:
    with open(FILE_PATH, "wb") as file:
        file.write(response.content)
    print(f"File saved: {FILE_PATH}")
else:
    print(f"Failed to download file, status code: {response.status_code}")
    exit(1)

# Git commands to push to GitHub
GIT_COMMIT_MESSAGE = f"Update VWRP holdings - {DATE_STR}"

subprocess.run(["git", "add", FILE_PATH])
subprocess.run(["git", "commit", "-m", GIT_COMMIT_MESSAGE])
subprocess.run(["git", "push"])
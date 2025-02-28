import requests
import datetime
import os
from bs4 import BeautifulSoup

# Define the base URL for Vanguard holdings
VANGUARD_URL = "https://www.vanguard.co.uk/professional/product/etf/equity/9679/ftse-all-world-ucits-etf-usd-accumulating"

# Get today's date to generate the filename pattern
today = datetime.datetime.today().strftime("%d_%m_%Y")
file_name_pattern = f"Holdings details - Vanguard FTSE All-World UCITS ETF (USD) Accumulating - {today}.xlsx"

# Function to find the latest holdings file URL
def get_holdings_file_url():
    response = requests.get(VANGUARD_URL, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print("Failed to retrieve page")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all links on the page
    for link in soup.find_all("a", href=True):
        if "Holdings details" in link.text and link["href"].endswith(".xlsx"):
            return link["href"]
    
    print("Could not find the file link.")
    return None

# Function to download the latest holdings file
def download_holdings_file(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(os.getcwd(), file_name_pattern)
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {file_name_pattern}")
        return file_path
    else:
        print("Failed to download file.")
        return None

# Execute script
if __name__ == "__main__":
    file_url = get_holdings_file_url()
    if file_url:
        download_holdings_file(file_url)

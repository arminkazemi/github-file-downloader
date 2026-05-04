from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.chrome.service import Service
import time
import os

# Create directory for HTML files
os.makedirs('html_snapshots', exist_ok=True)

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

# driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
# driver = webdriver.Chrome(driver_path, options=chrome_options)
driver = webdriver.Chrome(service=chrome_service,options=chrome_options)

url = "https://google.com"

print(f"Visiting: {url}")
driver.get(url)

# Wait for page to load
time.sleep(3)

# Save HTML
html_content = driver.page_source
filename = f"html_snapshots/snapshot_{int(time.time())}.html"

with open(filename, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Saved: {filename}")

# Wait before next URL
time.sleep(5)

driver.quit()
print("All snapshots saved!")

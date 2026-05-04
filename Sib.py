from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Use system ChromeDriver (already in PATH on ubuntu-latest)
driver = webdriver.Chrome(options=options)

# Create directory for HTML files
os.makedirs('html_snapshots', exist_ok=True)

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

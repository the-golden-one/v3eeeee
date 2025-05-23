import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without GUI
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get("https://www.aparat.com/v/bhi9lch")

print("Page Title:", driver.title)

# Keep the browser open and refresh every 30 minutes
while True:
    time.sleep(1800)  # Wait 30 minutes
    driver.refresh()
    print("Refreshed the page!")

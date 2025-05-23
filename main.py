from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Runs without GUI
options.add_argument("--no-sandbox")  # Required for some hosting environments

driver = webdriver.Chrome(options=options)
driver.get("https://www.aparat.com/v/YOUR_VIDEO_ID")

print("Page Title:", driver.title)

# Keep the browser running & refresh every 30 minutes
import time
while True:
    time.sleep(1800)  # Wait 30 minutes
    driver.refresh()
    print("Refreshed the page!")

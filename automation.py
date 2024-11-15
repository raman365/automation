from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging

# Setup logging to both console and file for improved error handling and visibility
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO to capture more detailed messages
    format='%(asctime)s - %(levelname)s - %(message)s',  # Add timestamp to logs
    handlers=[
        logging.FileHandler('app.log', mode='w'),  # Log to file
        logging.StreamHandler()  # Also log to console
    ]
)

# 1. Dynamic user input for search query
search_term = input("Enter your search query: ")

# 2. Chrome browser options for flexibility
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")  # Optional: Adjust window size for flexibility

# Automatically opens the browser with options
driver = webdriver.Chrome(options=chrome_options)

# Open Google
driver.get("https://www.google.com")
logging.info("Opened Google website")

# Wait for the page to load and cookies pop-up to appear
time.sleep(2)

# Find and click the "Accept All" button using its id attribute
try:
    accept_button = driver.find_element(By.ID, "L2AGLb")
    accept_button.click()
    logging.info("Clicked 'Accept All' button")
except Exception as e:
    logging.error("Accept All button not found or already accepted. Error: %s", str(e))

# Wait a moment for the action to complete
time.sleep(1)

# Find the search bar using its name attribute value
search_box = driver.find_element(By.NAME, "q")

# 1. Use the dynamic user-input search term
search_box.send_keys(search_term)
logging.info(f"Entered search term: {search_term}")

# Simulate hitting the "Enter" key to search
search_box.send_keys(Keys.RETURN)
logging.info("Performed search")

# Wait for the search results to load
time.sleep(2)

# Find the first search result link using its XPath and click it
try:
    first_result = driver.find_element(By.XPATH, '(//h3)[1]/ancestor::a')
    first_result.click()
    logging.info("Clicked the first search result.")
except Exception as e:
    logging.error("Failed to click the first search result. Error: %s", str(e))
    driver.save_screenshot("error_screenshot.png")  # Save a screenshot on error
    logging.info("Screenshot of error saved as 'error_screenshot.png'")

# Optional: Wait to see the action completed (for demonstration purposes)
time.sleep(2)

# Close the browser
driver.quit()
logging.info("Closed the browser and ended the session")

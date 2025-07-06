import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.google.com/maps/search/restaurants+in+Nairobi"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

print("Waiting for page to load...")
time.sleep(5) 

# --- SCROLLING LOGIC STARTS HERE ---

# Find the scrollable results panel
# This is usually the `div` with a role of `feed`
    # Scroll down 5 times to load more results
try:
    scrollable_div = driver.find_element(By.CSS_SELECTOR, "div[role='feed']")
    print("Scrolling to load more results...")
    for i in range(5): 
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        time.sleep(2)
except Exception as e:
    print("Could not find scrollable element.")



# --- DATA EXTRACTION STARTS HERE ---
results = driver.find_elements(By.CSS_SELECTOR, "div[jsaction*='mouseover:pane']")
print(f"Found {len(results)} results. Starting data extraction...")

scraped_data = []
for result in results:
    try:
        # Find the single element that contains all the details
        details_element = result.find_element(By.CSS_SELECTOR, ".fontBodyMedium")
        details_text = details_element.text
        image_url = result.find_element(By.CSS_SELECTOR, "img").get_attribute("src")

        # IMPORTANT: Skip if the text block is empty
        if not details_text:
            continue

        # Split the text block into lines
        parts = details_text.split('\n')
        
        # Assign parts to variables, with checks to prevent errors
        name = parts[0] if len(parts) > 0 else "N/A"
        rating = parts[1] if len(parts) > 1 else "N/A"
        address = parts[2] if len(parts) > 2 else "N/A"
        
        # Add the clean data to our list
        scraped_data.append([name, rating, address, image_url])
        
    except Exception:
        # If any other error occurs for a listing, just skip it
        continue
driver.quit()

# --- DATAFRAME CREATION AND EXPORT STARTS HERE ---
print(f"Data extraction complete. Found {len(scraped_data)} valid restaurants.")
print("Exporting to Excel...")

df = pd.DataFrame(scraped_data, columns=["Restaurant Name", "Rating/Price", "Address/Type", "Image URL"])
df.to_excel("restaurants_nairobi.xlsx", index=False)
print("Data exported successfully to restaurants_nairobi.xlsx")


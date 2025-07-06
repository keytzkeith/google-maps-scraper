# Google Maps Restaurant Scraper

This project is a Python script that scrapes Google Maps for restaurant data in a specified location. It uses Selenium to automate browser actions, handle dynamic content, and extract key information for a list of restaurants.

---

## 📜 Project Description

The primary goal of this project was to build a data scraper capable of navigating a dynamic, JavaScript-heavy website like Google Maps. The script automates the process of searching for restaurants, scrolling to load all results, and then extracting specific data points for each listing. The final, structured data is then exported to an Excel file for easy analysis.

---

## ✨ Key Features

- **Dynamic Scraping:** Uses Selenium to control a Chrome browser, allowing it to handle "infinite scroll" and other dynamically loaded content.
- **Data Extraction:** Scrapes the following data for each restaurant:
    - Name
    - Rating & Number of Reviews
    - Address / Type of Business
    - Image URL
- **Error Handling:** Implements `try-except` blocks to gracefully handle missing information for certain listings without crashing the script.
- **Data Export:** Exports the clean, structured data into a `.xlsx` file using the pandas library.

---

## 🛠️ Technologies Used

- **Python 3**
- **Selenium:** For web browser automation and scraping dynamic content.
- **pandas:** For data manipulation and exporting to Excel.
- **webdriver-manager:** To automatically manage the browser driver.

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [your-repository-link]
    ```
2.  **Install dependencies:**
    ```bash
    pip install selenium pandas webdriver-manager
    ```
3.  **Run the script:**
    ```bash
    python gmaps_scraper.py
    ```
    The script will create a file named `nairobi_restaurants.xlsx` upon completion.

---

## 💻 Code Snippet

Here is a snippet showing the core logic for scrolling through the results page to load all listings before extraction.

```python
# --- SCROLLING LOGIC ---
try:
    scrollable_div = driver.find_element(By.CSS_SELECTOR, "div[role='feed']")
    print("Scrolling to load more results...")
    # Scroll down 5 times to load more results
    for i in range(5):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        time.sleep(2) # Wait for new results to load
except Exception as e:
    print("Could not find scrollable element.")

📊 Sample Output

Below is a screenshot of the final Excel file containing the scraped restaurant data.

(./assets/data overview sample.png)

⚖️ Disclaimer

This script was created for educational purposes as a portfolio project. It is not intended for commercial use. Scraping Google Maps is against their Terms of Service, and this project was completed with respect for their infrastructure by using long delays and scraping only a small amount of publicly available data.
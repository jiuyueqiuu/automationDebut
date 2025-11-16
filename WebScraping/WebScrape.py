from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

"""
selenium is the Python library for automating browsers. You can control Chrome, Firefox, Edge, etc., programmatically.

webdriver is the main module for creating a browser instance and interacting with it.

Service is a class used to tell Selenium where the ChromeDriver binary is located. 
ChromeDriver is a small program that acts as a bridge between Selenium and the Chrome/Chromium browser.

Options is a class that allows you to configure Chrome’s settings, like headless mode, sandboxing, or window size.
"""

website = "https://www.thesun.co.uk/sport/football/"

service = Service("/snap/bin/chromium.chromedriver")  # your snap chromedriver

"""
Explanation:

Here you’re creating a Service object pointing to the chromedriver binary installed via Snap.

Snap installs binaries under /snap/bin/. In WSL, Snap automatically sets up the ChromeDriver executable here.

Selenium needs this because it can’t talk to Chrome/Chromium directly—it talks through ChromeDriver.

service is an object that tells Selenium where the ChromeDriver program is located.
"""

options = Options()
options.add_argument("--headless")          # no GUI
options.add_argument("--no-sandbox")        # required in some Linux setups
options.add_argument("--disable-dev-shm-usage")  # avoid /dev/shm issues

"""
options is an object that configures how Chrome runs.

It lets you set flags like headless mode, window size, disabling GPU, etc.

Think of options like telling Chrome:

“Chrome, open, but don’t show a window, don’t use the sandbox, and don’t rely on shared memory.”

Why we need it in WSL/Linux:
• WSL doesn’t have a GUI by default, so --headless prevents Chrome from crashing.
• --no-sandbox avoids permission issues in WSL.
• --disable-dev-shm-usage prevents crashes related to limited shared memory.
"""

driver = webdriver.Chrome(service=service, options=options)
"""
Here’s what happens when you combine them:
1. service tells Selenium which ChromeDriver to use.
2. options tells Chrome how to run (headless, no sandbox, etc.).
With this, Selenium opens chrome
"""

driver.get(website)

"""
driver.get(...) tells the already-open Chrome browser to go to the website you specify.
"""

print(driver.title)
driver.quit()


"""
print(driver.title) retrieves the title of the current webpage (the text that appears in the browser tab) 
and prints it to the console.

driver.quit() closes the browser completely and ends the Selenium session, freeing up system resources.
"""




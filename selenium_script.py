import os
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def download_chromedriver():
    # Define the URL to download Chrome WebDriver
    url = 'https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip'

    # Define the directory to store Chrome WebDriver
    driver_dir = os.path.join(os.getcwd(), 'chromedriver')

    print("Driver_dir:", driver_dir)

    # Create the directory if it doesn't exist
    os.makedirs(driver_dir, exist_ok=True)

    # Define the path to save the downloaded zip file
    zip_file_path = os.path.join(driver_dir, 'chromedriver.zip')

    

    # Download Chrome WebDriver zip file
    with open(zip_file_path, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)
    
    print(zip_file_path)

    # Extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(driver_dir)

    print("Driver_dir:", driver_dir)
    # Remove the zip file
    #os.remove(zip_file_path)

    # Set the executable permission to Chrome WebDriver
    os.chmod(os.path.join(driver_dir, 'chromedriver'), 0o775)
    print(os.path.join(driver_dir, 'chromedriver'))

    return os.path.join(driver_dir, 'chromedriver')

try:
    # Download Chrome WebDriver
    chromedriver_path = download_chromedriver()

    # Initialize Chrome WebDriver with service
    service = Service(chromedriver_path)
    service.start()

    # Initialize Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--detach')

    # Initialize Chrome WebDriver with Chrome options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    username = "pasupathikumar819@gmail.com"
    password = "MSpk@819"

    # Open MongoDB login page
    driver.get('https://cloud.mongodb.com/v2#/login')

    # Wait for the login page to load
    time.sleep(5)

    # Find username and password fields and fill them with credentials
    username_field = driver.find_element_by_id('Email Address')
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('Password')
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the dashboard page to load
    time.sleep(10)

    # Switch to the Atlas page where you can see your clusters
    driver.get('https://cloud.mongodb.com/v2#/atlas/register/cluster')

    # Wait for the clusters page to load
    time.sleep(5)

except Exception as e:
    print('Error:', e)
finally:
    # Close the browser window
    #driver.quit()
    print('MongoDB is not able to connect.')

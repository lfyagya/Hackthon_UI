from selenium import webdriver
import time
import requests
from config.config import CAL_TOKEN, BASE_URL, API_URL, CLIENT_ID
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

# Function to make API call and retrieve tokens
def get_tokens(client_id):
    url = API_URL
    params = {
        'clientId': CLIENT_ID,
        'token': CAL_TOKEN
    }

    response = requests.get(url, params=params)
    print(response)

    if response.status_code == 200:
        data = response.json()['data']  # Access the 'data' key
        accessToken = data['accessToken']
        refreshToken = data['refreshToken']
        return accessToken, refreshToken
    else:
        print("Error while fetching tokens:", response.text)
        return None, None

# Function to set cookies with tokens
def set_cookies(driver, accessToken, refreshToken):
    driver.add_cookie({'name': 'accessToken', 'value': accessToken})
    driver.add_cookie({'name': 'refreshToken', 'value': refreshToken})


# Main function to perform login and access the URL
def main():
    # Initialize Selenium WebDriver
    # chrome_options = Options()
    # chrome_options.add_argument("--user-data-dir=selenium_session")
    # driver = webdriver.Chrome()
    driver.maximize_window()

    client_id = CLIENT_ID

    # Get tokens from API
    accessToken, refreshToken = get_tokens(client_id)

    if accessToken and refreshToken:
        # Navigate to the desired URL (assuming it requires login)
        driver.get(BASE_URL)

        # Store tokens in cookies
        set_cookies(driver, accessToken, refreshToken)

        # Now, navigate to the desired URL
        driver.get(BASE_URL+"/events-notices/events?referencePeriod=upcoming")
        time.sleep(10)
    else:
        print("Failed to retrieve tokens. Exiting.")


if __name__ == "__main__":
    main()

driver.quit()
import public
from selenium import webdriver
import time
import requests

from config.config import Config
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
test_config = Config()
class Login:

    # Function to make API call and retrieve tokens
    def get_tokens(self, client_id, cal_token):
        url = test_config.API_URL
        params = {
            'clientId': client_id,
            'token': cal_token
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
    def set_cookies(self, driver, accessToken, refreshToken):
        driver.add_cookie({'name': 'accessToken', 'value': accessToken})
        driver.add_cookie({'name': 'refreshToken', 'value': refreshToken})

    # Main function to perform login and access the URL
    def run(self):
        service_object = Service(binary_path)
        driver = webdriver.Chrome(service=service_object)
        login = Login()
        driver.maximize_window()

        client_id = test_config.CLIENT_ID
        cal_token = test_config.CAL_TOKEN

        # Get tokens from API
        accessToken, refreshToken = (login.get_tokens(client_id, cal_token))
        # print(accessToken, refreshToken)

        if accessToken and refreshToken:
            # Navigate to the desired URL (assuming it requires login)
            driver.get(test_config.BASE_URL)

            # Store tokens in cookies
            login.set_cookies(driver, accessToken, refreshToken)


            # # Now, navigate to the desired URL
            driver.get(test_config.BASE_URL)
            # time.sleep(10)
            return driver

        else:
            print("Failed to retrieve tokens. Exiting.")


if __name__ == "__main__":
    Login().run()

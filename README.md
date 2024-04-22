# Hackthon_UI
1. Project Name: Vyaguta 
2. Introduction: This is an internal application used by the People management team to manage the employees of the company. The application will help to track the detailed information, allocation, attendance, Goals, and evaluation of employees so that the people management team will plan and decide as needed.

# Git using SHH KEY
1. Install Git https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
2. Clone this repo git@github.com:lfyagya/Hackthon_UI.git
# PyCharm
1. Install PyCharm https://www.jetbrains.com/pycharm/
2. In PyCharm virtual environment set up Python 10 or above. PyCharm Preferences -> Search for Python Interpreter
  # Create virtual environment
  1. python -m venv venv
  # Activate virtual environment
  # On Windows
  1. venv\Scripts\activate
  # On macOS/Linux
  1. source venv/bin/activate
# Install Required Packages
1. pip install -r requirements.txt
  1. request: $ python -m pip install requests
  2.  dotenv: pip install python-dotenv
  3.   elenium: pip install -U selenium
# ChromeDriver
1. Download a ChromeDriver that matches your Chrome browser version also if your Mac has M1 chip, download "mac64_m1.zip"
2. Unpack a chromedirver zip
3. Open Go -> Computer, make hidden files and folders visible
4. Move chromedriver file to usr -> local -> bin
5. Open a file. You should see "ChromeDriver was started successfully".
# How to run tests?
1. In a PyCharm terminal enter "pytest tests/test_leapfroggers.py -s -v"


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

def lambda_handler(event, context):

    options = Options()
    options.binary_location = '/var/task/headless-chromium/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/var/task/chromedriver/chromedriver',chrome_options=options)

    start = datetime.now()
    driver.get('https://www.telkomsel.com/prabayar')
    WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_id("kenapa-telkomsel-prabayar"))
    searchField = driver.find_element_by_id("kenapa-telkomsel-prabayar")
    print("searchField: {}".format(searchField.text))

    stop = datetime.now()
    thetime = stop - start
    print(thetime)

    driver.close();
    driver.quit();

    print('kampret')

    response = {
        "statusCode": 200,
        "body": thetime.seconds
    }

    return response

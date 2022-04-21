import urllib.request

urllib.request.urlretrieve("https://github.com/pm356/checking/raw/main/selenium.zip", "selenium.zip")

urllib.request.urlretrieve("https://github.com/pm356/checking/raw/main/webdriver_manager.zip", "webdriver_manager.zip")

import shutil
shutil.unpack_archive('selenium.zip')
shutil.unpack_archive('webdriver_manager.zip')


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.python.org")

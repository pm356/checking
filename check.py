
import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

def should_install_requirement(requirement):
    should_install = False
    try:
        pkg_resources.require(requirement)
    except (DistributionNotFound, VersionConflict):
        should_install = True
    return should_install


def install_packages(requirement_list):
    try:
        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        if len(requirements) > 0:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
        else:
            print("Requirements already satisfied.")

    except Exception as e:
        print(e)
        
install_packages(['tk'])
from tkinter import messagebox
# install_packages(['selenium','webdriver-manager'])

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.python.org")

messagebox.showinfo("Information","Informative message")

print("hi")

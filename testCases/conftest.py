import os
from datetime import datetime

import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
   if browser == 'edge':
      options = webdriver.EdgeOptions()
      options.add_experimental_option("detach", True)
      driver = webdriver.Edge(options=options)
      print("Launching Edge browser.........")
   elif browser == 'firefox':
      options = webdriver.FirefoxOptions()
      driver = webdriver.Firefox(options=options)
      print("Launching firefox browser.........")
   else:
      options = webdriver.ChromeOptions()
      options.add_experimental_option("detach", True)
      driver = webdriver.Chrome(options=options)
      print("Launching chrome browser.........")
   return driver
def pytest_addoption(parser):    # This will get the value from CLI /hooks
   parser.addoption("--browser")
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
   return request.config.getoption("--browser")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
   config.option.htmlpath = (os.path.dirname(os.getcwd()) + "\\tutorialNinjaV1\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")
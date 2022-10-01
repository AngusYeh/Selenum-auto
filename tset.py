# -*- coding: utf-
from selenium import webdriver
import os

os.environ["PATH"] = r"C:\SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://www.google.com")

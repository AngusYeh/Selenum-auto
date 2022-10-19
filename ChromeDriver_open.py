# -*- coding: utf-
from selenium import webdriver
import os

#設定chromedriver.exe 路徑，driver的版本要隨時更新，以免不支援。
os.environ["PATH"] = r"C:\SeleniumDrivers"

driver = webdriver.Chrome()
driver.get("https://www.google.com")

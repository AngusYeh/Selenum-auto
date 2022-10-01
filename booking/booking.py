# -*- coding: utf-8 -*-

import booking.contant as cont
import os
from selenium import webdriver
from  booking.bookingfilter import bookingfilter
from booking.report_hotel import report_list
from prettytable import PrettyTable


class booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] = self.driver_path
        super(booking ,self).__init__()
        #增加等候時間&視窗大小設定
        self.implicitly_wait(15)
        self.maximize_window()
        
    #設定讀取失敗的行為
    def __exit__(self,exc_type,exc_value,exc_tb):
        if self.teardown:
            self.quit()
        
    def homepage(self):
        self.get(cont.base_url)
        
    def choose_currency(self,currency=None):
        elem1 = self.find_element_by_css_selector(
            'button[data-tooltip-text="選擇您使用的幣別"]')
        elem1.click()
        
        elem2 = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        elem2.click()
    
    def select_place(self,place):
        elem1 = self.find_element_by_id('ss')
        elem1.clear()
        elem1.send_keys(place)
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]')
        first_result.click()
        
    def check_date(self,check_in,check_out):
        elem1 = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]')
        elem1.click()
        
        
        elem2 = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]')
        elem2.click()
        
    def select_adults(self,count):
        elem1 = self.find_element_by_id('xp__guests__toggle')
        elem1.click()
        
        while True:
            
            decrease =self.find_element_by_css_selector(
            'button[aria-label="減少成人的數量"]')
            decrease.click()
            
            adult_vaule = self.find_element_by_id('group_adults')
            value = adult_vaule.get_attribute('value')
            
            if int(value) == 1 :
                break
        
        increase = self.find_element_by_css_selector(
            'button[aria-label="增加成人的數量"]')
        for _ in range(count-1):
            increase.click()
    
    def search_page(self):
        search_ = self.find_element_by_css_selector(
            'button[type="submit"]')
        search_.click()
    
    def apply_filter(self,*ptr):
        
        filgter1 = bookingfilter(driver= self)
        filgter1.apply_star_rating(ptr)
        
    def sort_score_and_price(self):
        sort_ = self.find_element_by_css_selector(
            'li[data-id="review_score_and_price"]')
        sort_.click()
        
    def report(self):
        res = self.find_element_by_id(
            'search_results_table'
            ).find_elements_by_class_name('d20f4628d0')
        
        result = report_list(res)
        
        table = PrettyTable(
            field_names = ["Hotel_name","Hotel_score","Hotel_price"])
        table.add_rows(result.get_list())
        print(table)
        
        #print(result.get_list())
       
        
        
        
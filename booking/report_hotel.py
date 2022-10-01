from selenium.webdriver.remote.webelement import WebElement


class report_list():
    def __init__(self,list_element:WebElement):
        self.list_element = list_element
        
        

    def get_list(self):        
        output_list = []
        
        for hotel_name in self.list_element:
            lists__hotel_name = hotel_name.find_elements_by_class_name('fcab3ed991'
                                                           )[0].get_attribute("innerHTML").strip()
            lists_hotel_score = hotel_name.find_element_by_class_name('b5cd09854e'
                                                           ).get_attribute("innerHTML").strip()
            lists__hotel_cost = hotel_name.find_elements_by_class_name('fcab3ed991'
                                                           )[1].get_attribute("innerHTML").strip()
           
            output_list.append([lists__hotel_name,lists_hotel_score,lists__hotel_cost])
       
        return output_list
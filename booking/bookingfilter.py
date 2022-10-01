from selenium.webdriver.remote.webdriver import WebDriver

class bookingfilter():
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def apply_star_rating(self,stars):

        for star_rating in stars:
            
            class_star = self.driver.find_element_by_css_selector(
                f'div[data-filters-item="class:class={star_rating}"]')
            class_star.click()
        
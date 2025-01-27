from utility.lib  import SeleniumWrapper
from utility.excel import read_locator

class Wish_list:
    
    _locator=read_locator("wishlist")
    _locatorbo= read_locator("paymentpage")

    def __init__(self,driver):
        self.driver=driver


    def wishlist(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._locatorbo['a_book'])
        s.click_element(self._locator['lnk_text_book'])
        s.click_element(self._locator['btn_add_wish'])



from utility.lib  import SeleniumWrapper
from utility.excel import read_locator

class Wish_list:
    
    _locator=read_locator("")


    def __init__(self,driver):
        self.driver=driver


    def wishlist(self):
        s=SeleniumWrapper(self.driver)
        s.click_element()

        
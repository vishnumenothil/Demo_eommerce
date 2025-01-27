from utility.lib import SeleniumWrapper
from utility.excel import read_locator
class Homepage:

    _locator=read_locator("homepage")
    _loc_pay=read_locator('paymentpage')
    _loc_wish=read_locator("wishlist")
    def __init__(self,driver) -> None:
        self.driver=driver
                                                                                                             
    def login(self):
       s=SeleniumWrapper(self.driver)
       s.click_element(self._locator['lnk_login'])
       

    
    def register(self):
       s=SeleniumWrapper(self.driver)
    #    s.click_element(("link text","Register"))
       s.click_element(self._locator["lnk_register"])
    
    def shopping_cart(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._loc_pay['a_shopping_cart'])

    def logout(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._locator['a_logout'])
    

    def wishlist(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._loc_wish['ink_wishlist'])
        
    
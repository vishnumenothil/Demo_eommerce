
from utility.excel import read_locator
from utility.lib import SeleniumWrapper
class Shopping_cart:
    _locator=read_locator('paymentpage')
    def __init__(self,driver):
        self.driver=driver
    
    def shopping_cart(self,quantity,item):
       s=SeleniumWrapper(self.driver)
       if item == "book":
            s.text_clear(self._locator['txt_quat_book'])
            s.enter_text(self._locator['txt_quat_book'],value=quantity)
       elif item == "computer":
           s.text_clear(self._locator['txt_quat_com'])
           s.enter_text(self._locator['txt_quat_com'],value=quantity)

       s.click_element(self._locator['chk_agree'])
       s.click_element(self._locator['btn_check'])
       

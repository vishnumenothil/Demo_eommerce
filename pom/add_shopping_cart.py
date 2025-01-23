
from utility.lib import SeleniumWrapper
from utility.excel import read_locator
class Add_Shopping_cart:
    _locator=read_locator("paymentpage")
    print(_locator)
    def __init__(self,driver):
        self.driver=driver

    def add_shopp_cart(self,item):
        s=SeleniumWrapper(self.driver)
        if item == 'book':
            s.click_element(self._locator['a_book'])
            s.click_element(self._locator['btn_add_to_cart'])
        elif item == "computer":
            s.click_element(self._locator['a_compuer'])
            s.click_element(self._locator['a_notebooks'])
            s.click_element(self._locator['btn_add_to_cart_cpt'])

    # def shopping_cart_link(self):
    #     s=SeleniumWrapper(self.driver)
    #     s.click_element(self._locator['a_shopping_cart'])
        
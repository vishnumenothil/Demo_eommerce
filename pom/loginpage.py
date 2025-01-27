
from utility.lib  import SeleniumWrapper
from utility.excel import read_locator

class loginpage:
     
    _locators=read_locator("loginpage")
   
    print(_locators)
    def __init__(self,driver) -> None:
            self.driver=driver

     
    def login(self,email,password):
        s=SeleniumWrapper(self.driver)
        s.enter_text(self._locators["txt_email"],value=email)
        s.enter_text(self._locators["txt_password"],value=password)
        s.click_element(self._locators['btn_login'])


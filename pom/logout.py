
from utility.lib import SeleniumWrapper
from utility.excel import read_locator
class Logout:
    _locator=read_locator('logout') 
    def __init__(self,driver):
        self.driver = driver

    def  logout(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._locator['a_logout'])
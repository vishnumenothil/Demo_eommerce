
from utility.excel import read_locator
from utility.lib import SeleniumWrapper
from utility.lib import SeleniumWrapper
from pytest import mark
from pom.loginpage import loginpage
from pom.homepage import Homepage
from utility.excel import read_headers,read_data
from pom.wishlist import Wish_list 
import time

class Test_Whislist:
    
    read_locator('homepage')
    def test_wishlist(setup_tear_down):
        driver=setup_tear_down
        wish = Wish_list(driver)
        wish.wishlist()
        home=Homepage(driver)
        home.wishlist()
        time.sleep(2)
        
    
    
    
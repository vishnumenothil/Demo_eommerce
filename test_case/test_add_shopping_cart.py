from pytest import mark
from pom.homepage import Homepage
from utility.excel import read_headers
from utility.excel import read_data
from pom.loginpage import loginpage
from pom.logout import Logout
from pom.registrationpage import registration
from time import sleep
from pom.add_shopping_cart import Add_Shopping_cart
from pom.shopping_cart import Shopping_cart


header=read_headers("test_shopping","shopping1")
data=read_data("test_shopping","shopping1")
@mark.parametrize(header,data)
def test_shopping(setup_tear_down,email,password,item,itemname,quantity):
    driver=setup_tear_down
    home=Homepage(driver)
    home.login()
    lobj=loginpage(driver)
    lobj.login(email,password)
    # print(driver.title)
    if driver.title == 'Demo Web Shop':
        assert True
    else:
        driver.get_screenshot_as_file("screenshot/screenshot.png")

        assert False
    shope=Add_Shopping_cart(driver)
    shope.add_shopp_cart(item)
    # sleep(5)

    # shope.shopping_cart_link()
    home.shopping_cart()
    
    
    sho_qua=Shopping_cart(driver)
    sho_qua.shopping_cart(quantity,item)
    
    # l_out=Logout(driver)
    # l_out.logout()
    sleep(5)
    
    
    

    

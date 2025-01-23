
from utility.lib import SeleniumWrapper
from pytest import mark
from pom.loginpage import loginpage
from pom.homepage import Homepage
from utility.excel import read_headers,read_data
from pom.payment import Payment
from pom.shopping_cart import Shopping_cart
class Test_Payment:

    header=read_headers("test_payment","shopping1")
    data=read_data("test_payment","shopping1")
    @mark.parametrize(header,data)
    def test_payment(self,setup_tear_down,fname,lname,address,phone,cvv,card_no,city,pin_code,country,email,password,credit_cart,exp_mon,exp_year):
        driver=setup_tear_down
        
        home=Homepage(driver)
        home.login()

        log=loginpage(driver)
        log.login(email,password)

        home.shopping_cart()
        
        shope = Shopping_cart(driver)
        shope.shopping_cart(phone,cvv)

        pay= Payment(driver)
        pay.payment(fname,lname,address,phone,cvv,card_no,city,pin_code,country,credit_cart,exp_mon,exp_year)
        
        if driver.current_url == 'https://demowebshop.tricentis.com/checkout/completed/':
            assert True
        else:
            driver.get_screenshot_as_file("screenshot/payment.png")
            assert False

        print(driver.current_url)
       




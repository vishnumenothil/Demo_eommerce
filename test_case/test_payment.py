
from utility.lib import SeleniumWrapper
from pytest import mark
from pom.loginpage import loginpage
from pom.homepage import Homepage
from utility.excel import read_headers,read_data
from pom.payment import Payment
from pom.shopping_cart import Shopping_cart
from utility.logger import LoggGen
class Test_Payment:
    logger=LoggGen.loggen()
    header=read_headers("test_payment","shopping1")
    data=read_data("test_payment","shopping1")
    @mark.parametrize(header,data)
    def test_payment(self,setup_tear_down,fname,lname,address,phone,cvv,card_no,city,pin_code,country,email,password,credit_cart,exp_mon,exp_year):
        self.logger.info("**********************payment_test********************")
        driver=setup_tear_down
        
        home=Homepage(driver)
        home.login()

        log=loginpage(driver)
        log.login(email,password)
        self.logger.info("**********************successfully_login***********************")

        home.shopping_cart()
        
        shope = Shopping_cart(driver)
        shope.shopping_cart(phone,cvv)
        self.logger.info("******************successfully_item added to shopping cart******************")


        pay= Payment(driver)
        pay.payment(fname,lname,address,phone,cvv,card_no,city,pin_code,country,credit_cart,exp_mon,exp_year)
        
        if driver.current_url == 'https://demowebshop.tricentis.com/checkout/completed/':
            assert True
            self.logger.info("**********successfully payment placed**************")
 
        else:
            driver.get_screenshot_as_file("screenshot/payment.png")
            self.logger.info("**********failed payment**********8")
            assert False
            
        print(driver.current_url)
       





from utility.lib import SeleniumWrapper
from pytest import mark
from pom.loginpage import loginpage
from pom.homepage import Homepage
from utility.excel import read_headers,read_data
from utility.logger import LoggGen
from utility.veryfy_text import verify_text
headers=read_headers("test_login_positive","smoke")
data=read_data("test_login_positive","smoke")

@mark.parametrize(headers,data)
def test_login(setup_tear_down,_config,request,email,password):
    log=LoggGen.loggen()
    log.info("***********test loging*************")
    s=SeleniumWrapper(setup_tear_down,)
    homepage=Homepage(setup_tear_down)
    homepage.login()    
    lobj= loginpage(setup_tear_down)
    lobj.login(email,password) 
    verify_text(setup_tear_down,"Log out") 
    
   

headers1=read_headers("test_login_negative","smoke")
data_n=read_data("test_login_negative","smoke")
@mark.parametrize(headers1,data_n)
def test_login_negative(setup_tear_down,email,password):
    homepage=Homepage(setup_tear_down)
    homepage.login()
    lobj=loginpage(setup_tear_down)
    lobj.login(email,password)
    verify_text(setup_tear_down,"Log out") 
    
#     assert "dashboard" in setup_tear_down.current_url, "User not redirected to dashboard after valid login."




































































































































































































































































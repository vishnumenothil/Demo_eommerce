

from selenium.webdriver.chrome.webdriver  import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver  import WebDriver as Fairfox
from selenium.webdriver.edge.webdriver  import WebDriver as Edge
from selenium.webdriver.safari.webdriver  import WebDriver as Safari
from pytest import fixture





env="test"
browserr="edge"
class TestConfiguration:
    url="https://demowebshop.tricentis.com/"
    # email="vishnumenothil@gmai.com"

    # password="vishnu7902"
    ...

class StageConfiguaration :
    url="https://demowebshop.tricentis.com/"
    # email="stage@gmail.com"
    # password="stage123"
    ...


def pytest_addoption(parser):#pytest_addoptions it is built in method which is used to take input from the command 
                             #parser - it is  a built in fixture and an object also using to call method addoption  present in the class which created object by name parser  
    parser.addoption("--browser",action="store",dest="browser",default="chrome")
    parser.addoption("--env",action="store",dest="env",default="test")#--browser using to take value from the command prompt
    # parser.addoption("--time",action="store",dest="time",default="10")dest- where the value get stord that we are taking from the command this variable we can use in the progrme further
                                                                     #default- to give default value




@fixture
def  _config(request): #the value that taken from the command stored in local scope ,to accessvalue from the local variable we are using request
    if request.config.option.env.upper() == "TEST":
        print("test environment")
        return TestConfiguration
    elif request.config.option.env.upper() == "STAGE":
         print("stage environment")
         return StageConfiguaration
    else:
        raise Exception("unknown envronment")


@fixture
def setup_tear_down(request,_config):
    
    if request.config.option.browser.upper() == "CHROME" :
     driver= Chrome()             
    elif request.config.option.browser.upper() == "EDGE" :
        driver=Edge()
    elif request.config.option.browser.upper() == "SAFARI" :
        driver=Safari()
    driver.maximize_window()
    # driver.get("https://demowebshop.tricentis.com/")
    driver.get(_config.url)

    yield driver
    driver.close()







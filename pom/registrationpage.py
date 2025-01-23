from utility.lib import SeleniumWrapper
from pom.homepage import Homepage
from utility.excel import read_locator

class registration:
    _locator=read_locator("registrationpage")
    def __init__(self,driver) -> None:
         self.driver=driver

    def register(self,gender,fname,lname,email,password,confirmpassword):
        s=SeleniumWrapper(self.driver)
        
        # s.click_element(("link text","Register"))
        if gender.upper()=="MALE":
            s.click_element(self._locator['rdo_male'])
        elif gender.upper() == "FEMALE":
            s.click_element(self._locator['rdo_female'])

        else:
            raise Exception("unknown gender")
    
        s.enter_text(self._locator['txt_fname'],value=fname)
        s.enter_text(self._locator['txt_lname'],value=lname)
        s.enter_text(self._locator['txt_email'],value=email)
        s.enter_text(self._locator['txt_password'],value=password)
        s.enter_text(self._locator['txt_confirmpassword'],value=confirmpassword)
        s.click_element(self._locator['btn_register']) 
from utility.lib  import SeleniumWrapper
from utility.excel import read_locator
import time
class Payment:
    _locator=read_locator("paymentpage")
    def __init__(self,driver):
        self.driver=driver
    
    def  except_bl(self,fname,lname,address,phone,cvv,card_no,city,pin_code,country,credit_cart,exp_mon,exp_year):
            s=SeleniumWrapper(self.driver)
            s.click_element(self._locator['btn_continue1'])
            s.click_element(self._locator['btn_continue2'])
            s.click_element(self._locator['btn_continue3'])
            s.click_element(self._locator['rad_cred'])
            s.click_element(self._locator['btn_continue4'])

            s.select_item(self._locator['selct_cardtype'],item=credit_cart)
            s.enter_text(self._locator['txt_cardname'],value=fname)
            s.enter_text(self._locator['txt_cardno'],value=card_no)
            s.select_item(self._locator['sele_exp_mon'],item=exp_mon)
            s.select_item(self._locator['sele_exp_year'],item=exp_year)
            s.enter_text(self._locator['txt_code'],value=cvv)
            
            s.click_element(self._locator['btn_continue5'])
            s.click_element(self._locator['btn_confirm'])
            

    def payment(self,fname,lname,address,phone,cvv,card_no,city,pin_code,country,credit_cart,exp_mon,exp_year):
        
        s=SeleniumWrapper(self.driver)
        
        try:
            s.text_clear(self._locator['txt_add_fname'])
            s.enter_text(self._locator['txt_add_fname'],value=fname)
            s.text_clear(self._locator['txt_add_lname'])
            s.enter_text(self._locator['txt_add_lname'],value=lname)
            s.text_clear(self._locator['txt_add1'])
            s.enter_text(self._locator['txt_add1'],value=address)
            s.select_item(self._locator["coun_select"],item=country)
            s.enter_text(self._locator['txt_city'],value=city)
            s.enter_text(self._locator['txt_pin'],value=pin_code)
            s.enter_text(self._locator['txt_ph_no'],value=phone)
            self.except_bl(fname,lname,address,phone,cvv,card_no,city,pin_code,country,credit_cart,exp_mon,exp_year)
            # s.click_element(self._locator['btn_continue1'])
            # s.click_element(self._locator['btn_continue1'])
            # s.click_element(self._locator['btn_continue2'])
            # s.click_element(self._locator['btn_continue3'])
            # s.click_element(self._locator['rad_cred'])
            # s.click_element(self._locator['btn_continue4'])

            # s.select_item(self._locator['selct_cardtype'],item=credit_cart)
            # s.enter_text(self._locator['txt_cardname'],value=fname)
            # s.enter_text(self._locator['txt_cardno'],value=card_no)
            # s.select_item(self._locator['sele_exp_mon'],item=exp_mon)
            # s.select_item(self._locator['sele_exp_year'],item=exp_year)
            # s.enter_text(self._locator['txt_code'],value=cvv)
            
            # s.click_element(self._locator['btn_continue5'])
            # s.click_element(self._locator['btn_confirm'])
            
        except:
            self.except_bl(fname,lname,address,phone,cvv,card_no,city,pin_code,country,credit_cart,exp_mon,exp_year)
            
            # s.click_element(self._locator['btn_continue1'])
            # s.click_element(self._locator['btn_continue2'])
            # s.click_element(self._locator['btn_continue3'])
            # s.click_element(self._locator['rad_cred'])
            # s.click_element(self._locator['btn_continue4'])

            # s.select_item(self._locator['selct_cardtype'],item=credit_cart)
            # s.enter_text(self._locator['txt_cardname'],value=fname)
            # s.enter_text(self._locator['txt_cardno'],value=card_no)
            # s.select_item(self._locator['sele_exp_mon'],item=exp_mon)
            # s.select_item(self._locator['sele_exp_year'],item=exp_year)
            # s.enter_text(self._locator['txt_code'],value=cvv)
            
            # s.click_element(self._locator['btn_continue5'])
            # s.click_element(self._locator['btn_confirm'])
            
            
            
        
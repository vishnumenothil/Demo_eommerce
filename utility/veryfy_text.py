from utility.take_screenshot  import screenshot
from time import sleep

def verify_text (driver,etext):
    try:
        sleep(3)
        assert etext in driver.page_source
    except :
        screenshot(driver)
        assert False


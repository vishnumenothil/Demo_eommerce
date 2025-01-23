
from utility.excel import read_locator
from utility.lib import SeleniumWrapper
def test_wishlist(setup_tear_down):
    driver=setup_tear_down
    read_locator('homepage')
    
    
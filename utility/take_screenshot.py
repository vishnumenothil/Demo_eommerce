from datetime import datetime

def screenshot(driver):
    d=datetime.now().strftime("%d-%m-%y %H %H-%M-%S")
    driver.get_screenshot_as_file(f"screenshot/{d}.png")
    


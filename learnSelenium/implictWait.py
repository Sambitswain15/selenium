import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Chromedriver.exe")
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
count = len(driver.find_elements_by_xpath("//div[@class='product-action']"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:

    button.click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
code=driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")


driver.find_element_by_xpath("//button[@class='promoBtn']").click()
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
driver.quit()


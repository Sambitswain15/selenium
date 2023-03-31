from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://yahoo.com")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='ybar-sbq']").send_keys("bhubaneswar")
List_bhubaneswar = driver.find_elements_by_xpath("//ul[@role='listbox']/li")
for name in List_bhubaneswar:
    print(name.text)
 if name.text =="bhubaneswar to kolkata flight"
   name.click()


driver.sleep(2)
driver.quit()
# if "bhubaneswar" in List_bhubaneswar:
#    click()

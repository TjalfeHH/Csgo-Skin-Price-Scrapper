from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"chromedriver")

driver.get("https://store.steampowered.com/login/")

time.sleep(5)

driver.find_elements_by_class_name("newlogindialog_TextInput_2eKVn")[0].send_keys("TjalfeAPI")

time.sleep(5)

driver.find_elements_by_class_name("newlogindialog_TextInput_2eKVn")[1].send_keys("F1ndersKeeper")

driver.find_element_by_class_name("newlogindialog_SubmitButton_2QgFE").click()

time.sleep(15)

driver.get("https://steamcommunity.com/market/listings/730/Rio%202022%20Dust%20II%20Souvenir%20Package")

elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

print(source_code)

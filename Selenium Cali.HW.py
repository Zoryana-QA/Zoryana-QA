from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.find_element(By.XPATH,'//*[@class="site-title"]//*[@rel="home"]').get_attribute("href"))
print(driver.find_element(By.XPATH, '//*[@class="wp-image-55 size-full"]'). get_attribute("src"))

assert "California Real Estate" in driver.title
print (driver.title)

driver.find_element(By.ID, "send-us-a-message")
driver.find_element(By.ID, "g2-name"). send_keys("Aaa")
driver.find_element(By.ID, "g2-email"). send_keys("aaa@mail.com")
driver.find_element(By.ID, "contact-form-comment-g2-message"). send_keys("Hi all!")

driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').click()

time.sleep(3)

driver.find_element(By.CLASS_NAME,"link").click()
print(driver.find_element(By.CLASS_NAME,"pushbutton-wide").get_attribute('type'))

driver.quit()

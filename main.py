from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com.tr/?hl=tr")
sleep(3)
input = driver.find_element(By.NAME,"q") #name'e göre locate ol
input.send_keys("kodlama.io")
sleep(3)
searchButton = driver.find_element(By.CLASS_NAME,"gNO89b")
sleep(2)
searchButton.click()
sleep(3)
button = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
button.click()
sleep(7)

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")

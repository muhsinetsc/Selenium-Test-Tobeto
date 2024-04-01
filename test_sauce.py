from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_Sauce: 
    def precondition(self):
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")  
        return driver
    

    def test_invide_login(self):
        driver = self.precondition()
        userNameInput =driver.find_element(By.ID,"user-name")
        passwordInput =driver.find_element(By.ID,"password")        
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")        
        loginButton =driver.find_element(By.ID,"login-button")
        loginButton.click()        
        errorMassage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")        
        testResult = errorMassage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        
#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir. 
    def test_null_value(self):
        driver = self.precondition()
        loginButton =driver.find_element(By.ID,"login-button")
        loginButton.click()        
        expectedMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Username is required"
        print(f"Epic sadface: Username is required şeklinde uyarı mesajı gösterilmiştir = {testResult}")        
        
#-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir. 
    def test_null_password(self):
        driver = self.precondition()
        userNameInput =driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")        
        loginButton =driver.find_element(By.ID,"login-button")
        loginButton.click()        
        expectedMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testResult = expectedMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required şeklinde bir uyarı mesajı gösterilmiştir = {testResult}")

#-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
#"Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_user_locked(self):
        driver = self.precondition()
        userNameInput =driver.find_element(By.ID,"user-name")
        passwordInput =driver.find_element(By.ID,"password")       
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()       
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Epic sadface: Sorry, this user has been locked out. şeklinde uyarı mesajı gösterilmiştir = {testResult}")

#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_products_list(self):
        driver = self.precondition()
        userNameInput =driver.find_element(By.ID,"user-name")
        passwordInput =driver.find_element(By.ID,"password")       
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton =driver.find_element(By.ID,"login-button")
        loginButton.click()        
        driver.get("https://www.saucedemo.com/inventory.html")
        productList =driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı {len(productList)} adettir.")



testClass = Test_Sauce()
testClass.test_products_list()
testClass.test_user_locked()
testClass.test_null_password()
testClass.test_null_value()
testClass.test_invide_login()
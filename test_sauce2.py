from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait # ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
#bir zincir misali aksiyonları sıraya koymak


class Test_Sauce: 
    def precondition(self):
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        return driver
    
    def test_invalid_login(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMassage = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))     
        testResult = errorMassage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        
#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir. 
    def test_null_value(self):
        driver = self.precondition()
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Username is required"
        print(f"Epic sadface: Username is required şeklinde uyarı mesajı gösterilmiştir = {testResult}")        
        
#-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir. 
    def test_null_password(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput.send_keys("standard_user")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testResult = expectedMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required şeklinde bir uyarı mesajı gösterilmiştir = {testResult}")

#-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
#"Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_user_locked(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Epic sadface: Sorry, this user has been locked out. şeklinde uyarı mesajı gösterilmiştir = {testResult}")

#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_products_list1(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))       
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()        
        driver.get("https://www.saucedemo.com/inventory.html")
        productList =driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı {len(productList)} adettir.")


    def test_products_list2(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() #depoladığım aksiyonları çalıştır
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        """ baslik =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        testResult = baslik.text == "Swag Labs" """
        addToCart = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        driver.execute_script("window.scrollTo(0,500)")
        addToCart.click()
        """ actions2 = ActionChains(driver)
        actions2.move_to_element(addToCart) #butonun olduğu yere sayfayı taşı
        actions2.click()
        actions2.perform() """
        removeButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")))
        testResult = removeButton.text == "Remove"
        sleep(3)
        print(f"TEST SONUCU: {testResult}")


    def test_products_list2(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions.click(loginButton)
        actions.perform() #depoladığım aksiyonları çalıştır
        urunEkle1 = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        urunEkle2 = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-onesie']")))
        driver.execute_script("window.scrollTo(0,500)")
        urunEkle1.click()
        urunEkle2.click()
        sepet = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        actions.click(sepet).perform()
        removeButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")))
        actions.click(removeButton)
        checkout = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='checkout']")))
        actions.click(checkout)
        actions.perform()
        firstNAme = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        lastName = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"ulast-name")))
        zipCode = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        actions.send_keys_to_element(firstNAme,"Muhsine")
        actions.send_keys_to_element(lastName,"Tasci")
        actions.send_keys_to_element(zipCode,"123456")
        continueButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        actions.click(continueButton)
        actions.perform()
        finishButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"finish")))
        actions.click(finishButton).perform()
        sleep(4)
        baslik = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='checkout_complete_container]/h2")))
        testResult = baslik.text == "Thank you for your order!"
        sleep(3)
        print(f"Ödeme işlemi başarili: {testResult}")


    def dropDown(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions.click(loginButton)
        actions.perform() #depoladığım aksiyonları çalıştır
        #sıralama listesine tıklama
        dropDown = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        actions.click(dropDown)
        actions.perform()
        sleep(3)
        #sıralama listesinden indexe göre seçim yapma
        secme = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        sleep(1)
        select = Select(secme)
        select.select_by_index(3)
        # select.select_by_visible_text("Price (high to low)")
        # select.select_by_value("hilo")
        sleep(2)

    def menu(self):
        driver = self.precondition()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions.click(loginButton)
        actions.perform()
        menuButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
        actions.click(menuButton).perform()
        aboutLink = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"about_sidebar_link")))
        actions.click(aboutLink).perform()
        assert "saucelab" in driver.current_url, "Yanlis sayfadasin."
        print("Sauce Labs sayfasi acildi.")
        sleep(3)

 

                       
                               
# testClass = Test_Sauce()
# testClass.menu()      
# testClass.dropDown()
# testClass.test_products_list2()
# testClass.test_products_list1()
# testClass.test_user_locked()
# testClass.test_null_password()
# testClass.test_null_value()
# testClass.test_invalid_login()



     
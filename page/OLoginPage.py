import WebDriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import BasePage

class OLoginPage(BasePage.BasePage):
        elmUserName=(By.ID,"txtUsername")
        elmPassword=(By.ID,"txtPassword")
        elmLoginButton=(By.ID,"btnLogin")


        def __init__(self):
                self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),10)
                self.driver=WebDriverFactory.WebDriverFactory.getDriver()

        def navigateToLoginPage(self):
                self.driver.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/auth/login")
                return self

        def loginOrangeHRM(self,userName,Password):
                self.findElementBy(self.elmUserName).send_keys(userName)
                self.findElementBy(self.elmPassword).send_keys(Password)
                self.findElementBy(self.elmLoginButton).click()
                return self
        
                

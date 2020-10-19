from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name='email']")
    checkBox = (By.ID, "exampleCheck1")
    dropDown = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        #driver.find_element_by_css_selector("a[href*='shop']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.dropDown)

    def clickSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

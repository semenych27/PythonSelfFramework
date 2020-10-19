from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    chooseCountry = (By.LINK_TEXT, "Belarus")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "[type='submit']")
    confirmText = (By.CSS_SELECTOR, "[class*='alert-success']")

    def enteringCountryName(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectingCountryName(self):
        return self.driver.find_element(*ConfirmPage.chooseCountry)

    def selectingCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def clickSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def gettingConfirmText(self):
        return self.driver.find_element(*ConfirmPage.confirmText)
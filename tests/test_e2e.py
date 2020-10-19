import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        cards = checkOutPage.getCardTitles()
        log.info("getting all the card titles")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmpage = checkOutPage.checkOutItems()
        log.info("Entering country name as bel")
        enterCountryname = confirmpage.enteringCountryName().send_keys("Bel")
        self.verifyLinkPresence("Belarus")
        chooseCountry = confirmpage.selectingCountryName().click()
        selectingCheckBox = confirmpage.selectingCheckBox().click()
        clickingSubmitButton = confirmpage.clickSubmitButton().click()
        textMatch = confirmpage.gettingConfirmText().text
        log.info("Text received from application is " + textMatch)

        assert ("Success! Thank you!" in textMatch)




import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.clickCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.clickSubmitButton().click()
        alertText = homePage.getSuccessMessage().text
        assert "success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


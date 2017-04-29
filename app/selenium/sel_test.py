import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class FrontEndTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub/',
            desired_capabilities=DesiredCapabilities.CHROME
        )

        # create a new Chrome session
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://lb")

    def test010_signIn(self):
        signInButton = self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul[2]/li/a")
        signInButton.click()

        assert "Sign In" in self.driver.page_source

        username = self.driver.find_element_by_xpath("//*[@id=\"id_username\"]")
        password = self.driver.find_element_by_xpath("//*[@id=\"id_password\"]")

        username.send_keys("bob")
        password.send_keys("bob")

        submitButton = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[3]/button")
        submitButton.submit()

        assert "Welcome, Bob!" in self.driver.page_source

        self.driver.save_screenshot('signin.png')

    # def test020_searchEvent(self):
    #     self.test010_signIn()
    #     # # get the search textbox
    #     search_field = self.driver.find_element_by_name("query")
    #
    #     # enter search keyword and submit
    #     search_field.send_keys("adventure")
    #     search_field.submit()
    #     assert "Search Events" not in self.driver.page_source
    #
    #     self.driver.save_screenshot('sign.png')

    def test030_expDetailsPage(self):
        self.test010_signIn()

        exp = self.driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/a")
        exp.click()

        self.driver.save_screenshot('signin.png')

        assert "Experience Details" in self.driver.page_source

    def test040_userFlow(self):
        self.test010_signIn()

        dashButton = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/p[2]/a")
        dashButton.click()

        assert "User Dashboard" in self.driver.page_source

        createEventButton = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/div/a")
        createEventButton.click()

        assert "Create Event" in self.driver.page_source

        backButton = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/a")
        backButton.click()

        manageButton = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/a")
        manageButton.click()

        assert "My Events" in self.driver.page_source

        backButton = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/ol/li[2]/a")
        backButton.click()

        searchButton = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/a")
        searchButton.click()

        assert "Search Events" in self.driver.page_source

        homeButton = self.driver.find_element_by_xpath("/html/body/nav/div/div[1]/a")
        homeButton.click()

        assert "Welcome to GoX" in self.driver.page_source

    def test050_signOut(self):
        self.test010_signIn()

        signOutButton = self.driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul[2]/li[2]/a")
        signOutButton.click()

        assert "Sign In" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()

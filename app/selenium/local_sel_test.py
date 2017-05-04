import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FrontEndTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # create a new Chrome session
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://localhost:80/")

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
        

    def test020_searchEvent(self):
        self.test010_signIn()
        # # get the search textbox
        search_field = self.driver.find_element_by_name("query")

        # enter search keyword and submit
        search_field.send_keys("adventure")
        search_field.submit()
        assert "Search Events" in self.driver.page_source

    def test030_expDetailsPage(self):
        self.test010_signIn()

        exp = self.driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/a")
        exp.click() 

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

    def test060_createEvent(self):
        self.test010_signIn()

        dashButton = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/p[2]/a")
        dashButton.click()

        createEventButton = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/div/a")
        createEventButton.click()

        eventTitle = self.driver.find_element_by_xpath("//*[@id=\"id_title\"]")
        eventTitle.send_keys("Test event")

        eventDate = self.driver.find_element_by_xpath("//*[@id=\"id_date\"]")
        eventDate.send_keys("02012005")

        eventTime = self.driver.find_element_by_xpath("//*[@id=\"id_time\"]")
        eventTime.send_keys(Keys.ARROW_UP)
        eventTime.send_keys(Keys.ARROW_RIGHT)
        eventTime.send_keys(Keys.ARROW_UP)
        eventTime.send_keys(Keys.ARROW_RIGHT)
        eventTime.send_keys(Keys.ARROW_UP)
        eventTime.send_keys(Keys.ARROW_RIGHT)

        eventPrice = self.driver.find_element_by_xpath("//*[@id=\"id_price\"]")
        eventPrice.send_keys("100.00")

        eventDescription = self.driver.find_element_by_xpath("//*[@id=\"id_description\"]")
        eventDescription.send_keys("Event to test create event functionality")

        # send_keys needs the full file path to the picture
        # there are two slashes to escape the backslash used in windows file paths
        eventPic = self.driver.find_element_by_xpath("//*[@id=\"id_image\"]")
        eventPic.send_keys(os.path.dirname(os.path.realpath(__file__)) + "\\butterfly-wallpaper-5875-6202-hd-wallpapers.jpg") # gets current directory and adds the picture name to end
        # eventPic.send_keys("C:\\Users\\Jessi\\Desktop\\test_webdriver\\butterfly-wallpaper-5875-6202-hd-wallpapers.jpg")

        createButton = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[7]/button")
        createButton.click()

        assert "User Dashboard" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()


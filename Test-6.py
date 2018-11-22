import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/prithvigundabolu/Desktop/swetha/ISQA4900/chromedriver")

    def test6(self):
        user = "Team3"
        pwd = "isqa4900"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://bookinator-team3.herokuapp.com/")  # navigates to site
        time.sleep(2)

        # Login page
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)  # verifies login
        assert "WELCOME,Team3"
        time.sleep(2)

        # click sell books
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div[2]/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)

        # Edit added book
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[11]/a").click()
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("AAedited -Django 2 By Example")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "AAedited -Django 2 By Example"

        # click on buy books
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a").click()
        time.sleep(2)
        # click on used books
        elem = driver.find_element_by_xpath(
            "//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        assert "AAedited -Django 2 By Example"

        # clicks on the book
        elem = driver.find_element_by_xpath("//*[@id=\"main\"]/div[4]/h3[1]/a").click()
        assert "AAedited -Django 2 By Example"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

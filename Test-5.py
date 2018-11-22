import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/prithvigundabolu/Desktop/swetha/ISQA4900/chromedriver")

    def test5(self):
        user = "Team3"
        pwd = "isqa4900"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://bookinator-team3.herokuapp.com/")  # navigates to site
        time.sleep(2)

        # Logs in
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
        # click add book
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        # fill in details
        elem = driver.find_element_by_id("id_category")
        elem.send_keys("ISQA-4900")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("AASSel Test -Django 2 By Example")
        elem = driver.find_element_by_id("id_author")
        elem.send_keys("Antonio Mele")
        elem = driver.find_element_by_id("id_edition")
        elem.send_keys("First")
        elem = driver.find_element_by_id("id_isbn")
        elem.send_keys("10000000000")
        elem = driver.find_element_by_id("id_price")
        elem.send_keys("50")
        elem = driver.find_element_by_id("id_sellername")
        elem.send_keys("test case1")
        elem = driver.find_element_by_id("id_selleremail")
        elem.send_keys("testcase@gmail.com")
        elem = driver.find_element_by_id("id_sellerphone")
        elem.send_keys("7776665555")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        assert "AASel Test -Django 2 By Example"

        # click on buy books
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a").click()
        time.sleep(3)
        # click on used books
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div[2]/div/div/p[2]/a").click()
        time.sleep(3)
        assert "AASel Test -Django 2 By Example"

        # clicks on the book
        elem = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/h3[1]/a").click()
        assert "AASel Test -Django 2 By Example"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestScript_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/jayanth/testscripts/venv/Lib/chromedriver.exe")

    def test_coupons(self):

        driver = self.driver
        #to  maximze the chrome

        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/admin")

        # Logging to admin page
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("team3")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("isqa4900")
        elem = driver.find_element_by_xpath("//*[@id=\"login-form\"]/div[3]/input")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[3]/table/tbody/tr/td[1]/a")
        elem.click()
        time.sleep(3)
        #Creating a new coupon


        elem = driver.find_element_by_id("id_code")
        elem.send_keys("thanksgiving2018")
        elem = driver.find_element_by_id("id_valid_from_0")
        elem.send_keys("11/19/2018")
        elem = driver.find_element_by_id("id_valid_from_1")
        elem.send_keys("10:00:00")
        elem = driver.find_element_by_id("id_valid_to_0")
        elem.send_keys("11/30/2018")
        elem = driver.find_element_by_id("id_valid_to_1")
        elem.send_keys("10:00:00")
        elem = driver.find_element_by_id("id_discount")
        elem.send_keys("10")
        elem = driver.find_element_by_id("id_active")
        elem.click()
        elem = driver.find_element_by_xpath("//*[@id=\"coupon_form\"]/div/div/input[1]")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[1]")
        elem.click()
        time.sleep(5)

        # adding coupon to a book
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div[2]/div/div/div/div[1]/div/div/p[2]/a")
        elem.click()
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div[1]/div/div/p[2]/a")
        elem.click()
        elem = driver.find_element_by_xpath("//*[@id=\"main\"]/div/h3/a")
        elem.click()
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/form/input[3]")
        elem.click()
        elem = driver.find_element_by_id("id_code")
        elem.send_keys("thanksgiving2018")
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/input[2]")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()



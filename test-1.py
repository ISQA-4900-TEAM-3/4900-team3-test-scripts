import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestScript_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/jayanth/testscripts/venv/Lib/chromedriver.exe")

    def test_register(self):

        driver = self.driver
        #to  maximze the chrome

        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/li/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/p/a")
        elem.click()
        time.sleep(1)


        #Creating a new user
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("jay1995")
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("jayanth")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("jtirupathi@unomaha.edu")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("jayanth1995")
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("jayanth1995")
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/p[6]/input")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/p/a")
        elem.click()



        #logging in as a user
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("jay1995")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("jayanth1995")
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div/form/p[3]/input")
        elem.click()
        time.sleep(10)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#test exporting all orders to a csv file

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):

        # user credentials
        user = "Team3"
        pwd = "isqa4900"

        #open window
        driver = self.driver
        driver.maximize_window()

        #go to admin page
        driver.get("https://bookinator-team3.herokuapp.com/admin/login/?next=/admin/")
        time.sleep(2)

        # log in
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        #click orders
        elem = driver.find_element_by_xpath("""//*[@id="content-main"]/div[5]/table/tbody/tr/th/a""").click()
        time.sleep(2)

        # check all boxes toggle
        elem = driver.find_element_by_xpath("""//*[@id="action-toggle"]""").click()
        time.sleep(2)

        #select Export to CSV
        elem = driver.find_element_by_name('action')
        for option in elem.find_elements_by_tag_name('option'):
            if option.text == 'Export to CSV':
                option.click()
                break
        time.sleep(2)

        # check ok
        elem = driver.find_element_by_xpath("""//*[@id="changelist-form"]/div[1]/button""").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

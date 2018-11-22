import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#test adding a book

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):

        #open window
        driver = self.driver
        driver.maximize_window()

        #go to home page
        driver.get("https://bookinator-team3.herokuapp.com/")
        time.sleep(2)

        #click buy books
        elem = driver.find_element_by_xpath("""//*[@id="app-layout"]/div/div/div[2]/div/div/div/div[1]/div/div/p[2]/a""").click()
        time.sleep(2)

        # click new books
        elem = driver.find_element_by_xpath("""//*[@id="app-layout"]/div/div/div/div[2]/div/div[1]/div/div/p[2]/a""").click()
        time.sleep(2)

        # click Django 1
        elem = driver.find_element_by_xpath("""//*[@id="main"]/div[1]/a/img""").click()
        time.sleep(2)

        #select a quantity of 2
        elem = driver.find_element_by_id('id_quantity')
        for option in elem.find_elements_by_tag_name('option'):
            if option.text == '2':
                option.click()
                break
        time.sleep(2)

        # click Add to Cart
        elem = driver.find_element_by_xpath("""//*[@id="content"]/div[1]/form/input[3]""").click()
        time.sleep(2)

        # click Checkout
        elem = driver.find_element_by_xpath("""//*[@id="content"]/p[2]/a[2]""").click()
        time.sleep(2)


        #fill order fields
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Bill")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Nye")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("bNye@unomaha.edu")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("1001 White Street")
        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys("68681")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        time.sleep(2)

        #click Place Order
        elem = driver.find_element_by_xpath("""//*[@id="content"]/form/p[7]/input""").click()
        time.sleep(2)

        # fill payment fields
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="braintree-hosted-field-number"]"""))
        elem = driver.find_element_by_xpath("""//*[@id="credit-card-number"]""")
        elem.send_keys("4111111111111111")

        driver.switch_to.default_content()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="braintree-hosted-field-cvv"]"""))
        elem = driver.find_element_by_xpath("""//*[@id="cvv"]""")
        elem.send_keys("123")

        driver.switch_to.default_content()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="braintree-hosted-field-expirationDate"]"""))
        elem = driver.find_element_by_xpath("""//*[@id="expiration"]""")
        elem.send_keys("1220")


        #switch back out of the iframe
        driver.switch_to.default_content()

        # click Place Order
        elem = driver.find_element_by_xpath("""//*[@id="payment"]/input[3]""").click()
        time.sleep(2)

        #show new order

        # user credentials
        user = "Team3"
        pwd = "isqa4900"

        # go to admin page
        driver.get("https://bookinator-team3.herokuapp.com/admin/login/?next=/admin/")
        time.sleep(2)

        # log in
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        # click orders
        elem = driver.find_element_by_xpath("""//*[@id="content-main"]/div[5]/table/tbody/tr/th/a""").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

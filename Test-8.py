import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       #Pre-defined variables
       user = "instructor"
       pwd = "instructor1a"
       category = "ISQA-4900"
       name = "test"
       author = "test"
       edition = "1st"
       isbn = "000000000"
       price = "100"



       #Opening browser & maximizing window
       driver = self.driver
       driver.fullscreen_window()


       #logging in to the admin page
       driver.get("http://127.0.0.1:8000/admin")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       assert "Logged In"


       #Adding a new Product
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[last()]/table/tbody/tr[2]/td[1]/a")
       elem.click()
       elem = driver.find_element_by_id("id_category")
       elem.send_keys(category)
       elem = driver.find_element_by_id("id_name")
       elem.send_keys(name)
       elem = driver.find_element_by_id("id_author")
       elem.send_keys(author)
       elem = driver.find_element_by_id("id_edition")
       elem.send_keys(edition)
       elem = driver.find_element_by_id("id_isbn")
       elem.send_keys(isbn)
       elem = driver.find_element_by_id("id_price")
       elem.send_keys(price)
       elem = driver.find_element_by_xpath("//*[@id=\"id_available\"]")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"product_form\"]/div/div/input[1]")
       elem.click()
       time.sleep(2)
       driver.get("http://127.0.0.1:8000/buybooks/shop/")
       time.sleep(3)
       assert "Posted New Product"


       #Deleting the last created Product
       driver.get("http://127.0.0.1:8000/admin/shop/product/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[last()]/td[1]/input")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[2]/label/select/option[2]")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[2]/button")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[4]")
       elem.click()
       time.sleep(3)
       assert "Deleted New Product"


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

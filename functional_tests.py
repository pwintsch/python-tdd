from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):   #

    def setUp(self):     #
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):   #
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #
#Edith has heard of a cool new todo app she goes to check out its home page
        self.browser.get('http://localhost:8000')

#She notices the page title  and header mention To-do Lists

        self.assertIn('To-Do', self.browser.title) 
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

#she is invited to enter a todo item straight away
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

# She types buy peacock feathers into a text box
        inputbox.send_keys('Buy Peacock feathers')

# When she hits enter the page updates displaying "by peacock feathers " as an item
        inputbox.send_keys(Keys.ENTER)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text=='1: Buy peacock feathers' for row in rows),"New to-item did not appear in table")

# There is a text box inviting her to add another item. She enters "use peacock feather to tie a fly"
        self.fail('Finish the test') #
# The page updates again and shows both items on a list

# Edith wonders whether the site will remember her lists but sees it has generated a unique URL for her
# There is text describing that

# Edith Visits the URL the list is still there

# Edith goes back to sleep

if __name__=='__main__': #
    unittest.main(warnings='ignore') #

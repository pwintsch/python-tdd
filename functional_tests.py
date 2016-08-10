from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):   #

    def setUp(self):     #
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):   #
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #
        

#Edith has haerd of a cool new todo app she goes to check out its home page

        self.browser.get('http://localhost:8000')

#She notices the page title  and header mention To-do Lists

        self.assertIn('To-Do', self.browser.title) #
        self.fail('Finish the test') #

#she is invited to enter a todo item straight away

# She types buy peacock feathers into a text box

# When she hits enter the page updates displaying "by peacock feathers " as an item

# There is a text box inviting her to add another item. She enters "use peacock feather to tie a fly"

# The page updates again and shows both items on a list

# Edith wonders whether the site will remember her lists but sees it has generated a unique URL for her
# There is text describing that

# Edith Visits the URL the list is still there

# Edith goes back to sleep

if __name__=='__main__': #
    unittest.main(warnings='ignore') #

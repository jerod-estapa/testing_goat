#! usr/local/bin/python3

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Margot has heard about a new to-do app online and goes to
        # the URL to check it out.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away.

        # She types "Buy new football" into the text box (Margot loves sports).

        # When she hits enter, the page updates, and now the page lists,
        # "#1: Buy new football" as an item in a to-do list.

        # There is still a text box asking her to enter another item. She enters,
        # "Buy a soccer ball, too" (Margot really loves sports).

        # The page updates again, and now shows both items on her list.

        # Margot wonders if the site will remember her list. Then, she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits the URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
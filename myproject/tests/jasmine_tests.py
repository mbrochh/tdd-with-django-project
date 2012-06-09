"""
This is one of the great advantages Django 1.4 brings in: Running Selenium
tests has never been easier!

For many months I have been struggeling to develop a good TDD habit for my
Javascript files. There is a great testing framework, Jasemine, but you need
a browser to execute those tests.

With the help of ``django-jasmine`` we can provide a URL ``/jasmine/`` which
we can access via Selenium. It will open your browser and run the tests and
it will be part of your normal Django test suite. There is no longer any
excuse to "forget" to run your Jasmine tests!

"""
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class JasmineSeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(JasmineSeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(JasmineSeleniumTests, cls).tearDownClass()
        cls.selenium.quit()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/jasmine/'))
        result = self.selenium.find_element_by_class_name('description')
        self.assertTrue('0 failures' in result.text)

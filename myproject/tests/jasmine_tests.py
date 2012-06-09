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
        self.assertTrue('0 failures' in result)

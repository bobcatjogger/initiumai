'''
Created on Sep 12, 2016

@author: gotbergj
'''

from selenium import webdriver


class WebDriver(object):
    def __init__(self, b_type='chrome'):
        if b_type == 'chrome':
            self.wd_path = './chromedriver'
        elif b_type == 'phantomjs':
            self.wd_path = './phantomjs'
        else:
            raise NotImplementedError("Not yet implemented web driver type.")
    
    def start_browser(self, url=None, session_id=None):
        if url is None:
            if self.wd_path == './chromedriver':
                self.browser = webdriver.Chrome(executable_path = self.wd_path)
            elif self.wd_path == './phantomjs':
                self.browser = webdriver.PhantomJS(executable_path = self.wd_path)
        elif session_id:
            self.browser = webdriver.Remote(command_executor=url, desired_capabilities={})
            self.browser.session_id = session_id     
        self.browser.implicitly_wait(5)

    def get_text(self, element):
        return self.browser.execute_script("""
            var parent = arguments[0];
            var child = parent.firstChild;
            var ret = "";
            while(child) {
                if (child.nodeType === Node.TEXT_NODE)
                    ret += child.textContent;
                child = child.nextSibling;
            }
            return ret;
            """, element)

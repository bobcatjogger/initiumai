'''
Created on Sep 17, 2016

@author: jacob
'''
from logging import getLogger
from selenium import webdriver


class WebDriver(object):
    '''
    classdocs
    '''

    def __init__(self, b_type='chrome'):
        '''
        Constructor
        '''
        self.l = getLogger('aia_log')
        self.b_type = b_type

        if b_type == 'chrome':
            self.wd_path = './web_drivers/chromedriver'
        elif b_type == 'phantomjs':
            self.wd_path = './web_drivers/phantomjs'
        else:
            raise NotImplementedError("Not yet implemented web driver type.")

    def start_browser(self, url=None, session_id=None):

        if url:
            if session_id:
                self.browser = webdriver.Remote(command_executor=url,
                                                desired_capabilities={})
                self.browser.session_id = session_id
        else:
            if self.b_type == 'chrome':
                self.browser = webdriver.Chrome(executable_path=self.wd_path)
            elif self.b_type == 'phantomjs':
                self.browser = webdriver.PhantomJS(executable_path=self.wd_path)

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

'''
Created on Sep 17, 2016

@author: jacob
'''
from logging import getLogger
from selenium import webdriver as wd

# use email/pass
EMAIL = 'jakegot@gmail.com'
PASSWD = 'YZ85tQ^netHK3Jba*'
IURL = 'https://www.playinitium.com/main.jsp'


class WebDriver(object):
    '''
    classdocs
    '''
    def __init__(self, b_type='chrome'):
        '''
        Constructor
        '''
        self.b_type = b_type
        self.running = False
        self.l = getLogger('iai')
        self.brow = None

        if b_type == 'chrome':
            self.wd_path = './web_drivers/chromedriver'
        elif b_type == 'phantomjs':
            self.wd_path = './web_drivers/phantomjs'
        else:
            raise NotImplementedError("Not yet implemented web driver type.")
        self.start()

    def start(self, url=None, session_id=None):
        if self.running:
            self.l.debug('WD already started')
            return False

        if url:  # try to reconnect to an existing session
            if session_id:
                self.brow = wd.Remote(command_executor=url,
                                      desired_capabilities={})
                self.brow.session_id = session_id
        else:  # start a new browser
            if self.b_type == 'chrome':
                self.brow = wd.Chrome(executable_path=self.wd_path)
                self.l.debug('WD chrome started')
            elif self.b_type == 'phantomjs':
                self.brow = wd.PhantomJS(executable_path=self.wd_path)
                self.l.debug('WD phantomjs started')

        self.brow.implicitly_wait(5)  # how log to wait/retry
        self.brow.set_window_size(300, 500)  # resize the window
        self.brow.set_window_position(0, 0)  # move the window
        self.brow.get(IURL)
        self.l.debug('Launched main site')

        self.brow.find_element_by_xpath('//*[@id="signup-pane"]/p[1]/a').click()
        self.l.debug('Hit login')

        email_ele = self.brow.find_element_by_xpath('//*[@id="login-form"]/div[1]/input')
        pass_ele = self.brow.find_element_by_xpath('//*[@id="login-form"]/div[2]/input')

        email_ele.send_keys(EMAIL)
        pass_ele.send_keys(PASSWD)
        self.brow.find_element_by_xpath('//*[@id="login-form"]/div[3]/a').click()
        self.l.debug('Logging in')
        # Dump out session info for reconnect
        self.url = self.brow.command_executor._url
        self.session_id = self.brow.session_id
        self.l.debug('url: {} | session_id: {}'.format(self.url, self.session_id))

        self.running = True

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

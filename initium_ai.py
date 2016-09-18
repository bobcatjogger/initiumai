'''
Created on Sep 12, 2016

@author: gotbergj
'''

from web_driver import WebDriver

class InitiumAI(object):
    def __init__(self, browser_type='chrome'):
        self.browser_type = browser_type
        self.main_url = 'https://www.playinitium.com/main.jsp'
        self.running = False
        self.location = 'unknown'

    def start(self):
        if self.running:
            print('Initium is already running.')
            return False

        self.wd = WebDriver(self.browser_type)
        self.wd.start_browser()
        print('web_driver started')
        
        # Resize the window to the screen width/height
        self.wd.browser.set_window_size(300, 500)
        
        # Move the window to position x/y
        self.wd.browser.set_window_position(0, 0)

        self.wd.browser.get(self.main_url)
        print('Launched main site')

        # use email/pass
        email = 'jakegot@gmail.com'
        passwd = 'YZ85tQ^netHK3Jba*'

        self.wd.browser.find_element_by_xpath('//*[@id="signup-pane"]/p[1]/a').click()
        print('Hit login')

        email_ele = self.wd.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]/input')
        pass_ele = self.wd.browser.find_element_by_xpath('//*[@id="login-form"]/div[2]/input')

        email_ele.send_keys(email)
        print('Email entered')
        pass_ele.send_keys(passwd)
        print('Pass entered')
        self.wd.browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/a').click()
        print('Logging in')
        # Dump out session info for reconnect
        self.url = self.wd.browser.command_executor._url
        self.session_id = self.wd.browser.session_id
        print(self.url, self.session_id)

        self.running = True

    def reconnect(self):
        # TODO: not working
        # static for testing
        url = 'http://127.0.0.1:49675'
        s_id = '110ccf4113e49cda9a6f9139133aad00'
        self.wd = WebDriver(self.browser_type)
        self.wd.start_browser(url, s_id)
        self.running = True
        return
    
    def status(self):
        try:
            if not self.running:
                print('Please start AIA first.')
                return

            # location_keeper
            location_ele = self.wd.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/a')
            self.location = self.wd.get_text(location_ele)
            print("Location: {}".format(self.location))

            # hp cur/max
            hp_raw = self.wd.browser.find_element_by_xpath('//*[@id="hitpointsBar"]/p')
            hp_raw = self.wd.get_text(hp_raw)
            self.hp_cur, self.hp_max = hp_raw.split('/')
            print('HP cur: {} / HP max: {}'.format(self.hp_cur, self.hp_max))

            # gold
            self.gold = self.wd.get_text(self.wd.browser.find_element_by_xpath('//*[@id="mainGoldIndicator"]'))
            print('Gold: {}'.format(self.gold))
            
            # stats
            str_raw = self.wd.get_text(self.wd.browser.find_element_by_xpath('//*[@id="reload-div"]/div/div[3]/div/div[1]/div'))
            self.str_base, self.str_cur = str_raw.split(' (')
            self.str_cur = self.str_cur[:-1]
            print('Str base: {} Str cur: {}'.format(self.str_base, self.str_cur))
            
            
        except Exception as doh:
            print("Something broke: {}".format(doh))

    def explore(self):
        pass
        # Dessert /html/body/div[3]/div[18]/a[2]
        # <a href="#" class="main-button" shortcut="69" onclick="doExplore(false)"><span class="shortcut-key">(E)</span>Explore Desert</a>
        # grand mountain /html/body/div[3]/div[17]/a[2]
        # <a href="#" class="main-button" shortcut="69" onclick="doExplore(false)"><span class="shortcut-key">(E)</span>Explore Grand Mountain</a>
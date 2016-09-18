'''
Created on Sep 12, 2016

@author: gotbergj
'''

from . import web_driver as WD
from logging import getLogger


class InitiumAI(object):
    def __init__(self, browser_type='chrome'):
        self.browser_type = browser_type
        self.main_url = 'https://www.playinitium.com/main.jsp'
        self.running = False
        self.location = 'unknown'
        self.l = getLogger('aia_log')

    def start(self):
        if self.running:
            self.l.debug('Initium is already running.')
            return False

        self.wd = WD.WebDriver(self.browser_type)
        self.wd.start_browser()
        self.l.debug('web_driver started')

        # Resize the window to the screen width/height
        self.wd.browser.set_window_size(300, 500)

        # Move the window to position x/y
        self.wd.browser.set_window_position(0, 0)

        self.wd.browser.get(self.main_url)
        self.l.debug('Launched main site')

        # use email/pass
        email = 'jakegot@gmail.com'
        passwd = 'YZ85tQ^netHK3Jba*'

        self.wd.browser.find_element_by_xpath('//*[@id="signup-pane"]/p[1]/a').click()
        self.l.debug('Hit login')

        email_ele = self.wd.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]/input')
        pass_ele = self.wd.browser.find_element_by_xpath('//*[@id="login-form"]/div[2]/input')

        email_ele.send_keys(email)
        self.l.debug('Email entered')
        pass_ele.send_keys(passwd)
        self.l.debug('Pass entered')
        self.wd.browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/a').click()
        self.l.debug('Logging in')
        # Dump out session info for reconnect
        self.url = self.wd.browser.command_executor._url
        self.session_id = self.wd.browser.session_id
        self.l.debug(self.url, self.session_id)

        self.running = True

    def reconnect(self):
        # TODO: not working
        # static for testing
        url = 'http://127.0.0.1:55303'
        s_id = '698a4b7acb86ebda2661b63afcd29fdc'
        self.wd = WD.WebDriver(self.browser_type)
        self.wd.start_browser(url, s_id)
        self.running = True
        return

    def status(self):
        try:
            if not self.running:
                self.l.debug('Please start AIA first.')
                return

            # location_keeper
            location_ele = self.wd.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/a')
            self.location = self.wd.get_text(location_ele)
            self.l.debug("Location: {}".format(self.location))

            # hp cur/max
            hp_raw = self.wd.browser.find_element_by_xpath('//*[@id="hitpointsBar"]/p')
            hp_raw = self.wd.get_text(hp_raw)
            self.hp_cur, self.hp_max = hp_raw.split('/')
            self.l.debug('HP cur: {} / HP max: {}'.format(self.hp_cur, self.hp_max))

            # gold
            self.gold = self.wd.get_text(self.wd.browser.find_element_by_xpath('//*[@id="mainGoldIndicator"]'))
            self.l.debug('Gold: {}'.format(self.gold))

            # stats
            str_raw = self.wd.get_text(self.wd.browser.find_element_by_xpath('//*[@id="reload-div"]/div/div[3]/div/div[1]/div'))
            self.str_base, self.str_cur = str_raw.split(' (')
            self.str_cur = self.str_cur[:-1]
            self.l.debug('Str base: {} Str cur: {}'.format(self.str_base, self.str_cur))

        except Exception as doh:
            self.l.debug("Something broke: {}".format(doh))

    def explore(self):
        pass

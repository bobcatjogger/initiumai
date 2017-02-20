'''
Created on Sep 12, 2016

@author: gotbergj
'''

from logging import getLogger


class InitiumAI(object):
    def __init__(self, browser_type='chrome'):
        self.browser_type = browser_type
        self.main_url = 'https://www.playinitium.com/main.jsp'
        self.running = False
        self.location = 'unknown'
        self.l = getLogger('aia_log')

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

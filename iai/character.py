'''
Created on Sep 23, 2016

@author: gotbergj
'''
from logging import getLogger


class Character(object):
    '''
    classdocs
    '''

    def __init__(self, wd):
        '''
        Constructor
        '''
        self.l = getLogger('iai')
        self.wd = wd

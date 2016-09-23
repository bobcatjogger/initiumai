'''
Created on Sep 12, 2016

@author: gotbergj
'''

import json


class Location(object):
    def __init__(self, name):
        self.links = {}
        self.name = name

    def link_loc(self, connected_loc):
        self.links[connected_loc.name] = connected_loc

    def connected_locs(self):
        return self.links


class LocationKeeper(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def load_locs_from_file(self, path_to_loc_file="locations.json"):
        pass

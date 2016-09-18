#! /usr/bin/python3
'''
Created on Sep 17, 2016

@author: jacob
'''

import argparse
from logging import getLogger
from iai import log
from iai import initium_ai


def main(wd):
    log.setup_log('./logs/iai')
    l = getLogger('aia_log')
    l.info('Starting Main')
    l.debug('debug test')
    l.error('testing errors')

    ai1 = initium_ai.InitiumAI(wd)

    while True:
        # wait for user input
        usr_in = input("Accepting commands: ")
        l.debug('AIA recieved {}'.format(usr_in))

        if usr_in.lower() in ['q', 'quit', 'exit']:
            l.debug('Exiting.')
            break
        elif usr_in.lower() in ['start', 'go']:
            # open up the browser, navigate to main site, and login
            ai1.start()
        elif usr_in.lower() in ['recon', 'reconnect']:
            # open up the browser, navigate to main site, and login
            ai1.reconnect()
        elif usr_in.lower() in ['s', 'status']:
            # open up the browser, navigate to main site, and login
            ai1.status()
        else:
            l.debug('Unknown command: {}'.format(usr_in))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', "--web_driver",
                        help=("Define which web driver to use "
                              "(defualt is 'chrome')."))
    args = parser.parse_args()
    if args.web_driver:
        wd = args.web_driver
    else:
        wd = 'chrome'

    main(wd)

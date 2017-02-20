#! /usr/bin/python3
'''
Created on Sep 17, 2016

@author: jacob
'''
import argparse
import logging

from iai import web_driver
from iai import character


def main(wd):
    # logging
    setup_log()
    l = logging.getLogger('iai')
    l.info('*** Started AIA ***')

    # open up the browser and log in
    wd = web_driver.WebDriver()

    # create a char
    c = character.Character(wd)

    # report status and location

    # start main loop
    l.info('*** All Done ***')
'''
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
'''


def setup_log():
    # create logger with 'spam_application'
    logger = logging.getLogger('iai')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler('./logs/info.log')
    fh.setLevel(logging.INFO)

    # create file handler which logs even debug messages
    dfh = logging.FileHandler('./logs/debug.log')
    dfh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    dfh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.addHandler(dfh)

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

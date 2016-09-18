'''
Created on Sep 17, 2016

@author: jacob
'''

import logging
import os


def setup_log(path='./logs/iai'):
    _ensure_path(path)
    logger = logging.getLogger('aia_log')
    logger.setLevel(logging.DEBUG)

    fmt_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    fmt = logging.Formatter(fmt_str)

    fh = logging.FileHandler('{}.info'.format(path))
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    db_fh = logging.FileHandler('{}.debug'.format(path))
    db_fh.setLevel(logging.DEBUG)
    db_fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(fmt)

    logger.info('***** Log setup complete *****')


def _ensure_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

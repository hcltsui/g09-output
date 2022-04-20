# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:47:16 2022

@author: nht45
"""

import logging
import logging.config

logging.config.fileConfig("logging.conf")

# logger = logging.getLogger("g09") 
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

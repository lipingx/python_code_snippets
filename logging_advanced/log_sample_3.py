import util
import logging

util.SetLogConfig('log_sample-3.log')
logging.info('test log in %s', __file__)

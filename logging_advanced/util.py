import logging

def SetLogConfig(log_file_name):
	# The log file will be in the current directory where you run this main file.
	logging.basicConfig(
	    level=logging.DEBUG,
	    format='%(asctime)s,%(levelname)-6s [%(filename)s:%(lineno)d] %(message)s',
	    filename=log_file_name,
	)

	# Set up logging to console besides store to log file.
	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	# Set a format which is simpler for console use
	formatter = logging.Formatter(
	    '%(asctime)s,%(levelname)-6s [%(filename)s:%(lineno)d] %(message)s')
	console.setFormatter(formatter)
	logger = logging.getLogger('')
	logger.addHandler(console)

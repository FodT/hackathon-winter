from __future__ import print_function
from terminalone import T1, filters
from terminalone.vendor import six
import configparser
import time
from functools import wraps

def retry (function, retry=3):
	@wraps(function)
	def	wrapper	(*args,	**kwargs):
		exception = None
		for i in range(retry):
			try:
				return function(*args, **kwargs)
			except Exception as ex:
				six.print_('failed, retrying')
				time.sleep(1)
				exception = ex
		raise exception
	return wrapper


def setup(credentials, use_json, api_base):
	t1 = T1(environment='sandbox',
			auth_method='cookie',
			api_base=api_base,
			json=use_json,
			**credentials)
	assert hasattr(t1, 'user_id'), 'No user ID present'
	return t1

def getStrategies(t1, campaignId, isRunning=None):
	strategies = t1.get('strategies', limit={'campaign': campaignId}, get_all=True)
	return strategies

def main():
	cfg = configparser.RawConfigParser()
	cfg.read('config')
	creds = {
		'username': cfg.get('sandbox', 'user'),
		'password': cfg.get('sandbox', 'pass'),
		'api_key': cfg.get('sandbox', 'api_key')
	}
	t1 = setup(creds, False, cfg.get('sandbox', 'api_url'))
	strategies = getStrategies(t1, 232170)
	for s in strategies:
		print(s.id)

def strategiesHandler(event, context): 
	return main()

if __name__ == '__main__':
	main()

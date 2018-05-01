# import secrets

class HTTPHeader(object):
	HOST = 'Host'
	RANGE = 'Range'

class DownloadRequest(object):
	
	# HEADER 
	# Other configs, ie: download limit, priority
	def __init__(self, url, destination, headers=None):
		if headers:
			self._headers = headers
		else:
			self._headers = dict()
		self._request_id = 0
		self._destination = destination
		self._url = url
		pass
		
	def set_headers(self, field=None, data=None, headers=None):
		if field and data:
			self._headers[field] = data
		if headers:
			self._headers.update(headers)
		
	def get_headers(self):
		return self._headers
		
	def get_destination(self):
		return self._destination
		
	def get_url(self):
		return self._url
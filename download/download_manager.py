import requests

class DownloadManager(object):
	
	def __init__(self):
		pass
		
	'''
	return response:dictionary, session
	'''
	def download(self, download_request):
		session = requests.Session()
		session.headers.update(download_request.get_headers())
		response = session.get(download_request.get_url(), stream=True)
		return response.iter_content(chunk_size=128)
	
	def get_header(self, download_request):
		return requests.options(download_request.get_url()).headers
	
import requests

class DownloadManager(object):
	
	@staticmethod
	def download(download_request):
		session = requests.Session()
		session.headers.update(download_request.get_headers())
		response = session.get(download_request.get_url(), stream=True)
		return response.iter_content(chunk_size=128)
	
	@staticmethod
	def get_header(download_request):
		return requests.options(download_request.get_url()).headers
	
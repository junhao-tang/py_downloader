from download.models import DownloadRequest, HTTPHeader
from download.download_manager import DownloadManager
import hashlib


class Downloader(object):
	def __init__(self, url, destination):
		# load config
		self.request = DownloadRequest(url, destination)
		self._load_config()
		pass
	
	def _load_config(self):
		self.hasher = hashlib.md5()
		
	def start_download(self):
		chucks = DownloadManager.download(self.request)
		with open(self.request.get_destination(), 'wb') as f:
			for chuck in chucks:
				if chuck:
					f.write(chuck)
					self.hasher.update(chuck)
					
	def set_download_range(self, min=None, max=None):
		if not min or min < 0:
			min = 0
		if not max or max <= min:
			max = ''
		range = 'bytes={min}-{max}'.format(min=str(min), max=str(max))	
		self.request.set_headers(field=HTTPHeader.RANGE, data=range)

	def hash(self):
		return self.hasher.hexdigest()
from download.models import DownloadRequest, HTTPHeader
from download.download_manager import DownloadManager
import hashlib


class Downloader(object):
	def __init__(self):
		# load config
		pass
		
	def start_download(self, url, destination):
		request = DownloadRequest(url, destination)
		download_manager = DownloadManager()
		chucks = download_manager.download(request)
		hasher = hashlib.md5()
		with open(destination, 'wb') as f:
			for chuck in chucks:
				if chuck:
					f.write(chuck)
					hasher.update(chuck)
		print(hasher.hexdigest())
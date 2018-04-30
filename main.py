import argparse
from pydownloader.downloader import Downloader

def main(args):
	Downloader().start_download(args.url, 'output.png')
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="Download url")

	args = parser.parse_args()
	main(args)


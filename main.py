import argparse
from pydownloader.downloader import Downloader

def main(args):
	if not args.url or not args.output:
		raise Exception
	downloader = Downloader(args.url, args.output)
	downloader.set_download_range(min=args.min, max=args.max)
	downloader.start_download()
	print('downloaded : {0}'.format(args.output))
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="Download url")
	parser.add_argument("-o", "--output", help="Output file")
	parser.add_argument("-n", "--min", help="Lowest byte range")
	parser.add_argument("-m", "--max", help="Highest byte range")

	args = parser.parse_args()
	main(args)


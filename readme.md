# OOXX1024
A high-speed Robust Torrent Download Package

# Install
You can install ooxx1024 with pip:

	pip install ooxx1024

Or download the source code and unzip. <br>Change your direction to the file then use following command:

	python setup.py install

Now, ooxx1024 is ready.

# Quickstart

Open a Python(3.x) Interpreter:

	from ooxx1024 import Downloader
	dl = Downloader()
	dl.start()
Leave it alone and do your stuff. Torrents will fill your disk soon.

The default save directory is C:\

### Stop Download

	dl.stop()
It may take seconds to come to a completely stop.

### Change Save Directory
	
	dl.save_dir = "C:/My/Secret/File/"

### Change Taste
The default taste of our downloader is "Asian1". 
Available tastes are listed in:

	dl.taste_list

Pick your favor, and told the downloader:

	dl.taste = "Animate"

### Use Proxies

This is an example, replace the details with your own proxy. 

	dl.proxies = "http://10.10.1.10:3128"
To use HTTP Basic Auth with your proxy, use the http://user:password@host/ syntax:

	dl.proxies = 'http://user:pass@10.10.1.10:3128/'

Or, implement global proxy settings to your computer(recommended).

__\*Warning\*:__ 
You should not trust our proxies setting feature, it is untested and not guaranteed.

# Trivials
+ New contributors are welcomed, PR is prefered.
+ 高速撸棒种子下载包，嗯，我喜欢这个简介。
import os
import re
import threading
from time import sleep
from configparser import ConfigParser

import requests
from bs4 import BeautifulSoup

_flag = False
_base_url = "http://www.t66y.com/"
_taste_params = {
	"亞洲無碼":"2",
	"亞洲有碼":"15",
	"歐美":"4",
	"動漫":"5",
	"Asian1":"2",
	"Asian2":"15",
	"Western":"4",
	"Animate":"5",
}

class TestException(Exception):
	pass


class OOXXException(Exception):
	pass


class RetrieveError(OOXXException):
	pass


class TasteError(OOXXException):
	pass



def illegal_name_filter(name):
	for i in r'*/\|<>:?"':
		name = name.replace(i, "_")
	return name


def fetch_torrent(taste="亞洲無碼", save_path="c:/"):
	global _flag
	url = _base_url + "thread0806.php"
	params = {"fid": _taste_params[taste]}
	
	request = requests.get(url, params)
	try:
		request.raise_for_status()
	except HTTPError:
		raise RetrieveError("Fail to retrieve 1024 webpage.")
	soup = BeautifulSoup(request.content, 'lxml')
	max_page = int(re.findall(r"page=(\d+)", soup.find("a", id="last")["href"])[0])
	
	for page in range(1, max_page-100):
		params["page"] = page
		request = requests.get(url, params)
		sleep(1)
		soup = BeautifulSoup(request.content, "lxml")
		a_list = soup.find_all('a')
		post_list = [{'title':a.string, 'href':a['href']} for a in a_list
			if "htm_data" in a.get('href',default="") and a.string!=".::"]
		
		regex = r'(http://www.rmdown.com/link.php\?hash=[a-z0-9]+)'
		
		for post in post_list:
			if _flag: return None
			request = requests.get(_base_url + post['href'])
			sleep(1)
			try:
				store_link = re.findall(regex, request.content.decode('gbk'))[0]
			except:
				continue
			request = requests.get(store_link)
			sleep(1)
			soup = BeautifulSoup(request.content, "lxml")
			
			magic = {
				ingredient['name']:ingredient['value'] for ingredient in soup.find_all('input')
				}
			torrent_link = 'http://www.rmdown.com/download.php'
			torrent = requests.get(torrent_link, magic)
			sleep(1)
			beatiful_seed = save_path + illegal_name_filter(post['title']) + ".torrent"
			if torrent.content!=b"No such file!!":
				with open(beatiful_seed, 'wb') as heiheihei:
					heiheihei.write(torrent.content)


class Downloader():
	def __init__(self, save_path="C:/", taste="亞洲無碼"):
		self._taste = taste
		self._taste_list = tuple(_taste_params.keys())
		self._save_path = save_path
		self._proxy = None
		self._thread = None
	
	@property
	def taste_list(self):
		return self._taste_list
	
	@property
	def taste(self):
		return self._taste
	
	@taste.setter
	def taste(self, mytaste):
		if mytaste not in self.taste_list:
			raise TasteError("Taste unacceptable, check Downloader.taste_list for more information")
		else:
			self._taste = mytaste
	
	@property
	def save_path(self):
		return self._save_path
	
	@save_path.setter
	def save_path(self, path):
		if not path:
			path = "C:/"
		path = path.replace("\\", "/")
		if path[-1]!="/":
			path += '/'
		if not os.path.exists(self.save_path):
			os.makedirs(path)
		self._save_path = path
	
	@property
	def proxy(self):
		return self._proxy
	
	@proxy.setter
	def proxy(self, myproxy):
		try:
			os.environ["HTTP_PROXY"] = myproxy
		except:
			pass
		self._proxy = myproxy

	def start(self):
		if self._thread:
			return None
		if not os.path.exists(self.save_path):
			os.makedirs(self.save_path)
		self._thread = threading.Thread(target=fetch_torrent, args=(self.taste, self.save_path))
		self._thread.start()
	
	def stop(self):
		global _flag
		_flag = True
		self._thread.join()
		self._thread = None

if __name__=="__main__":
	pass
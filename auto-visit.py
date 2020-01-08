#!/usr/bin/python2

from requests.exceptions import ConnectionError
import requests
import time
import sys
import os

M = '\033[1;31m'
K = '\033[1;32m'
H = '\033[1;33m'
P = '\033[1;34m'
U = '\033[1;35m'
A = '\033[1;36m'
C = '\033[1;37m'
W = '\033[90m'

def banner():
	print(''+C+'''
           _         _         __     ___     _ _             
          / \  _   _| |_ ___   \ \   / (_)___(_) |_ 
         / _ \| | | | __/ _ \   \ \ / /| / __| | __/ 
        / ___ \ |_| | || (_) |   \ V / | \__ \ | |
       /_/   \_\__,_|\__\___/     \_/  |_|___/_|\__\  
  '''+W+'Author : RandiOloy\n\t\t  YT : RANDI OLOYY')
                   
def main():
	success = []
	gagal = []
	headers = {
	'Connection' : 'keep-alive', 
	'User-Agent' : 'Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54', 
	'Accept' : 'image/webp,image/apng,image/*,*/*;q=0.8', 
	'Content-Type' : 'text/html; charset=UTF-8',
	}
	os.system('clear')
	os.system('xdg-open https://www.youtube.com/channel/UCbZ45S0QGbo5IAaItt-mBlA')
	c = 0
	banner()
	print
	f = raw_input(''+C+'MASUKKAN SITE'+W+' ('+H+' Ex : '+C+'https://www.site.com '+W+') : ')
	u = input(''+C+'JUMLAH VISIT'+W+' ('+H+' Ex : '+C+'100 '+W+') : ')
	print
	print(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	
	for i in range(u):
		try:
			if not f.startswith('http'):
				print(M+'Gunakan Http / Https !')
				break
			k = requests.get('{}'.format(f), headers=headers)
			c += 1
			q = success
			g = gagal
			if k.status_code < 200 or k.status_code <= 201:
				print(''+C+'Visitor Ke ' + W + str(c) + H + ' Success' + C + ' Dikirimkan')
				success.append(q) 
				
			else:
				print(''+C+'Visitor Ke ' + W + str(c) + A + ' Gagal' + C + ' Dikirimkan')
				gagal.append(g)
				
		except ConnectionError:
			print
			print(M+'Koneksi Error ')
			break
	
	print
	print(''+C+'----------- '+W+'Selesai & Hasil'+C+' -----------')
	h = (len(success))
	l = (len(gagal))
	print
	print(''+C+'Success : '+W+str(h))
	print(''+C+'Gagal : '+W+str(l))
	
	
	
if __name__ == '__main__':
	main()
			
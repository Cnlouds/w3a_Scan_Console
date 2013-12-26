#!/usr/bin/python
# vim: set fileencoding=utf-8:

import nmap

class Nmap_self_module:
	def __init__(self,Ip_list):
		self.Ip_list=Ip_list

	def make_rep(self,item):
		if item =="":
			return "None"
		elif item is None:
			return "None"
		else:
			return item

	def  nmap_do(self):
		nm=nmap.PortScanner()
		nm.scan(hosts=self.Ip_list,arguments='-T4 -O')
		for ip in nm.all_hosts():
			try:
				print ip
				print nm[ip]['status']['state']
				print nm[ip]['addresses']['mac']
				print nm[ip]['hostname']

				try:
					for  port in nm[ip]['tcp'].keys():
						print "port: "+ str(port) + " name: " + nm[ip]['tcp'][port]['name'] + " status: " + nm[ip]['tcp'][port]['state']
				except:
					print "tcp Error"

				try:
					for os in nm[ip]['osmatch']:
						print "name: "+os['name'] + " accuracy: "+os['accuracy']
				except:
					print "osmatch error"
			except:
				print "Update or status or mac Error"

# t=Nmap_self_module("192.168.31.0/24")
# t.nmap_do()
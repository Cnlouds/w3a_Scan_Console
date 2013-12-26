#!/usr/bin/python
# vim: set fileencoding=utf-8:

from BeautifulSoup import BeautifulSoup
import urllib2
import re

class Form_analy():
	def __init__(self,domain,target):
		self.domain=domain
		self.target=target

	def results(self):
		results=urllib2.urlopen(self.target).read()
		soup=BeautifulSoup(results)

		input_items=[]
		form_list_result=[]
		form_tmp_result={}

		for item in soup.findAll('form'):
			if re.match('^(http|http)://',item.get('action')):
				action=item.get('action')
			elif re.match('^/',item.get('action')):
				action=self.domain+item.get('action')
			else:
				action=self.domain+'/'+item.get('action')
			method=item.get('method')
			for input_item in item.findAll('input'):
				value=input_item.get('name')
				if value!=None:
					input_items.append(input_item.get('name'))
			form_tmp_result['action']=action
			form_tmp_result['method']=method.upper()
			form_tmp_result['item']=input_items
			input_items=[]
			form_list_result.append(form_tmp_result)
		form_tmp_result={}

		for item in soup.findAll('script'):
			for line in item:
				_tmp=[]
				form_tmp_result['method']=re.compile("type:\'(\w+)\'").findall(line)[0].upper()
				form_tmp_result['action']=re.compile("url:\'(.*)\'").findall(line)[0]
				item_results=re.compile("data:\{(.*)\}").findall(line)[0].split(',')
				for r in item_results:
					_tmp.append(r.split(':')[0])
				form_tmp_result['item']=_tmp
				form_list_result.append(form_tmp_result)

		if len(form_list_result)==0:
			return None
		else:
			return form_list_result

	def result_analy(self,text):
		array_item={}
		if self.results() !=None:
			for item in self.results():
				if item['method']=="POST":
					action=item['action']
					for tmp_item in item['item']:
						array_item[tmp_item]=text
					print array_item
					print action
				elif item['method']=="GET":
					print "GET anay"
				else:
					continue

t=Form_analy('http://192.168.31.168','http://192.168.31.168/a.html')
t.result_analy("a")
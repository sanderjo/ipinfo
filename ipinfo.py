#!/usr/bin/env python

'''
Based on this public API from http://ipinfo.io/ :

$ curl http://ipinfo.io/31.21.30.159/json
{
  "ip": "31.21.30.159",
  "hostname": "No Hostname",
  "city": "",
  "region": "",
  "country": "NL",
  "loc": "52.3667,4.9000",
  "org": "AS31615 T-mobile Netherlands bv."
}
'''

import json
import urllib
baseurl = 'http://ipinfo.io/'	# no HTTPS supported (without plan)


def getall(ipaddress):
	url = '%s%s/json' % (baseurl, ipaddress)
	try:
		urlresult = urllib.urlopen(url)
		jsonresult = urlresult.read()		# get the JSON
		parsedjson = json.loads(jsonresult)	# put parsed JSON into dictionary
		return parsedjson
	except:
		return None


def country_and_org(ipaddress):
	allinfo = getall(ipaddress)	# one lookup
	try:
		# FYI: the first word in allinfo['org'] is the ASN, which we skip
		return allinfo['country'] + ' --- ' + allinfo['org'].split(' ', 1)[1]
	except:
		return ""

def country_and_org_as_list(ipaddress):
	allinfo = getall(ipaddress)	# one lookup
	try:
		# FYI: the first word in allinfo['org'] is the ASN, which we skip
		return [ allinfo['country'], allinfo['org'].split(' ', 1)[1] ]
	except:
		return ['','']

if __name__ == '__main__':

	# Some examples:

	print getall('31.21.30.159')
	print country_and_org('31.21.30.159')

	print getall('192.168.0.1')
	print country_and_org('192.168.0.1')

	print country_and_org('2a00:1450:4013:c01::64')
	print country_and_org('::ffff:194.109.6.92')

	print ' --- '.join(country_and_org_as_list('31.21.30.159'))
	print ' --- '.join(country_and_org_as_list('31.21.30.'))






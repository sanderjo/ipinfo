# ipinfo
Python module to get info on IP address from ipinfo.io

# Usage

```
>>> import ipinfo

>>> print ipinfo.country_and_org('8.8.8.8')
US --- Google Inc.

>>> print ipinfo.getall('8.8.8.8')
{u'loc': u'37.3845,-122.0881', u'city': u'Mountain View', u'country': u'US', u'region': u'California', u'hostname': u'google-public-dns-a.google.com', u'ip': u'8.8.8.8', u'org': u'AS15169 Google Inc.', u'postal': u'94040'}

>>> print ipinfo.country_and_org('2001:888:0:18::80')
NL --- Xs4all Internet BV

```

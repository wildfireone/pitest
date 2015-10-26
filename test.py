import urllib2

req = urllib2.Request('http://www.google.com')
try: urllib2.urlopen(req)
except urllib2.URLError as e:
    print e.reason
else:
    print "site is up"
    code = urllib2.urlopen(req).getcode()
    print code
    if(code == 200):
        print "ok"
    else:
        print "broke" + str(code)

import urllib2;
 
request = urllib2.Request("http://www.baidu.com") 
response = urllib2.urlopen(request);
print response.read();


#参数传递 post /  get



#post
import urllib
import urllib2
 
values = {"username":"username","password":"123"};
data = urllib.urlencode(values) ;
url = "https://passport.csdn.com/account/login?from=http://my.csdn.net/my/baidu";
request = urllib2.Request(url,data);
response = urllib2.urlopen(request);
print response.read();


#get
import urllib
import urllib2
 
values={}
values['username'] = "username"
values['password']="XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
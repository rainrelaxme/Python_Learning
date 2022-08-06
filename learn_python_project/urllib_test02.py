from urllib import request


'''req =request.Request("http://fanyi.baidu.com")
response = request.urlopen(req)
html = response.read()
html = html.decode("utf-8")
print(html)'''

#request.urlretrieve("http://www.zzti.edu.cn/_mediafile/index/2017/06/24/1qjdyc7vq5.jpg"
#	,"aaa.jpg")

f = request.urlopen('http://fanyi.baidu.com')
data = f.read()
print('Status:', f.status, f.reason)
for k, v in f.getheaders():
	print('%s:%s' %(k,v))
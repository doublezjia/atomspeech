#coding=utf8
import requests

key = 'dc47ce10cfd24347a6e0baf08401d2d8'
def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
	    'key'    : key, # 如果这个Tuling Key不能用，那就换一个
	    'info'   : msg, # 这是我们发出去的消息
	    'userid' : 'wechat-robot', # 这里你想改什么都可以
	}
	# 我们通过如下命令发送一个post请求
	try:
		req = requests.post(apiUrl, data=data).json()
		if req.get('code') == 200000:
			return req.get('text')+'\n'+req.get('url')
		else:
			return req.get('text')
	except:
		return "QAQ 我出问题了"
	# 让我们打印一下返回的值，看一下我们拿到了什么

echo = '''
+-----------------------------------------------+
+                                               +
+	I am Atom ，你想问什么。                +
+                                               +
+	输入 q 退出。                           +
+                                               +
+-----------------------------------------------+
	'''
print (echo)
while True:
	msg = input("你想问什么:");
	if msg == 'q' :
		print ('Good Bye, man or lady')
		break;
	else :
		replay = get_response(msg);
		print (replay);
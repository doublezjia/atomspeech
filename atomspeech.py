#百度语音api测试
#Python安装api可以通过pip install baidu-aip进行安装
#
#要pip安装pygame和baidu-aip
#
#文档中心
#语音合成：http://yuyin.baidu.com/docs/tts/196
#语音识别：http://yuyin.baidu.com/docs/asr/190
#pygame播放音频：http://www.cnblogs.com/chan7/p/5801953.html
#图灵机器人：http://www.tuling123.com/
#
#

#引用百度语音的api 
from aip import AipSpeech
import requests,sys,time,pygame,itchat,os

#连接百度语音api
# 定义常量
# APP_ID API_KEY SECRET_KEY 通过注册百度语音api获得
APP_ID = '60801'
API_KEY = 'jFCtbpgdjK4AgGe8nqwspFwT7X6Q'
SECRET_KEY = 'DdVleovbIiw1fqeeTrZ'
# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


#连接图灵机器人
#这个key是图灵机器人的，通过注册图灵机器人获得
key = 'dc47ce10cfd24347a6e0baf08401d2d8'
def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
	    'key'    : key, # 如果这个Tuling Key不能用，那就换一个
	    'info'   : msg, # 这是我们发出去的消息
	    'userid' : 'Atom', # 这里你想改什么都可以
	}
	# 我们通过如下命令发送一个post请求
	try:
		req = requests.post(apiUrl, data=data).json()
		if req.get('code') == 200000 :
			return req.get('text')+'\n'+req.get('url')
		elif req.get('code') == 302000:
			new = ''
			for i in range(len(req.get('list'))):
				new =new+'\n标题：'+req.get('list')[i].get('article')+'\n地址：'+req.get('list')[i].get('detailurl')+'\n来源：'+req.get('list')[i].get('source')+'\n'
			return req.get('text')+'\n'+new
		else:
			return req.get('text')
	except:
		return 'QAQ Error'




#读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#出错时候的提示
def baidu_speech_Err():
	result  = aipSpeech.synthesis('出错啦！！！', 'zh', 1, {'vol': 5,'per':0,})
	if not isinstance(result, dict):
		with open(r'sound\auido.mp3', 'wb') as f:
			f.write(result)

#合成语音
def baidu_voice(msg):
	result  = aipSpeech.synthesis(msg, 'zh', 1, {'spd':3,'pit':5,'vol': 5,'per':0,})
	# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
		with open(r'sound\auido.mp3', 'wb') as f:
			f.write(result)
	else:
		baidu_speech_Err()


#主程序，识别语音并传到图灵机器人，返回数据合成语音。
# def baidu_speech():
# 	# 识别本地文件，aipSpeech 支持pcm（不压缩）、wav、amr的音频文件
# 	req=aipSpeech.asr(get_file_content(soundfile), 'pcm', 16000, {'lan': 'zh',})

# 	#识别错误代码
# 	reqerr_no=req['err_no']

# 	if reqerr_no == 0:
# 		#获取识别出来的文字
# 		# message=req['result'][0]
# 		message='广州天气'
# 		# 通过get_response来连接图灵机器人，实现信息返回。
# 		msg=get_response(message)
# 		try:
# 			baidu_voice(msg)
# 		except:
# 			baidu_speech_Err()
# 	else:
# 		baidu_speech_Err()

#这个是测试玩的。可以删了它，用上面的。
def baidu_speech(tip):
	message = tip
	msg=get_response(message)
	try:
		baidu_voice(msg)
	except:
		baidu_speech_Err()




#音频播放器，播放mp3音频
def vosic_play(music):
	vosicfile = music
	pygame.mixer.init()
	track = pygame.mixer.music.load(vosicfile)
	pygame.mixer.music.play()
	#通过死循环实现音乐播放，音乐完成后会跳出循环的。
	while pygame.mixer.music.get_busy():
		pass;

	pygame.mixer.music.stop()
	#为了方便重新加载auido.mp3这个音频，所以添加了个atom.mp3,解决auido.mp3被占用的问题。如果有更好的方法解决占用问题可以把这里删掉。
	pygame.mixer.init()
	track = pygame.mixer.music.load(r'sound\atom.mp3')

if __name__ == "__main__":
	#音源，这里的音频和Python文件在同一个目录下，所以不用注明路径,音频只能是pcm（不压缩）、wav、amr的文件。
	# soundfile='sound\testsound.wav'
	# music=r'sound\auido.mp3'
	# try:
	# 	baidu_speech()
	# 	vosic_play(music)
	# except:
	# 	baidu_speech_Err()


	# #这个是测试玩的，可以删了它，用上面的。
	# tiptxt = """
	# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# 	图灵机器人和百度语音测试

	# 	输入 演员 播放文件夹内的音乐，这个与语音和机器人无关。
	# 	输入 q 退出程序。
	# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# """
	# print (tiptxt)
	# while 1:
	# 	tip = input("输入内容：")
	# 	if tip == 'q':
	# 		sys.exit()
	# 	elif tip == '演员':
	# 		music=r'sound\yy.mp3'
	# 		try:
	# 			print ('music playing....')
	# 			vosic_play(music)
	# 			continue
	# 		except:
	# 			baidu_speech_Err()
	# 	else:	
	# 		try:
	# 			baidu_speech(tip)
	# 			vosic_play(music)
	# 			continue
	# 		except:
	# 			baidu_speech_Err()



	#itchat连接测试，这也是玩的。
	@itchat.msg_register(itchat.content.TEXT)
	def atom_play(msg):
		if msg['ToUserName'] !='filehelper':return
		if msg['Text'] == u'演员':
			music=r'sound\yy.mp3'
			itchat.send(u'music playing....','filehelper')
			try:
				vosic_play(music)
			except:
	 			baidu_speech_Err()
		elif msg['Text'] == '关机':
	 		os.system('shutdown -s -t 0')
		else:
			music=r'sound\auido.mp3'
			try:
				# itchat.send(msg['Text'],'filehelper')
				baidu_speech(msg['Text'])
				vosic_play(music)
			except:
				baidu_speech_Err()
	itchat.auto_login(True)
	itchat.run()


import requests
import json
from configparser import ConfigParser
from bs4 import BeautifulSoup
config = ConfigParser()
config.read("c:/Users/tulik/Desktop/Work_Python/TelegramBot/config.ini")
accesstoken=config.get('Credential','token')
telegrambot = 
# req = requests.get("https://www.indeed.co.in/jobs?q=python+developer&l=Pune,+Maharashtra&jt=fulltime&fromage=1").text
# soup = BeautifulSoup(req,'lxml')
# allJob_title = soup.find_all('a',class_="jobtitle turnstileLink")
# titles = [job.text.strip() for job in allJob_title]
# links = [job['href'] for job in allJob_title]
# companys = [job.text.strip() for job in soup.find_all('span',class_='company')]
# all_info = zip(titles,links,companys)
# for (t,l,c) in all_info:
# 	print(t,l,c)

class telegram_bot():
	def __init__(self,config):
		self.token = self.app_config_file(config)
		self.base = "https://api.telegram.org/bot{}".format(self.token)

	def get_updates(self,offset=None):
		url = self.base+"/getupdates?timeout=100"
		if offset:
			url = url + "&offset+1"
		request = requests.get(url)
		response = request.json()
		return response

	def send_message(self,chat_id,msg):
		url = self.base +"/sendMessage?chat_id={}&text={}".format(chat_id,message)
		if msg is not None:
			request = requests.get(url)
			
	def app_config_file(self,config):
		parser = ConfigParser()
		parser.read(config)
		return parser.get('Credential', 'token')

	
# def request_bot(url):
# 	try:
# 		request = requests.get(url)
# 		response = request.json()
# 		print(request.headers)
# 	except HttpError as http_response:
# 		print("Error occured : {}".format(http_response))
# 	except Exception as exp:
# 		print("Detail of exception : {}".format(exp))
# 	return response

# def bot_info():

# 	info = request_bot(telegrambot+"/getme")
# 	return info


# def bot_receive_msg():
# 	resp = request_bot(telegrambot+"/getUpdates")
# 	return resp

# def bot_send_message(message,chat_id):
# 	url = "{}/sendMessage?chat_id={}&text={}".format(telegrambot,chat_id,message)
# 	Bot_response = request_bot(url)
# 	return Bot_response

# def retrieve_LastMessage():
# 	list_msgs = bot_receive_msg()['result']
# 	len_list=len(list_msgs)
# 	last_msg= list_msgs[len_list-1]
# 	personid=last_msg['message']['from']['id']
# 	personName=last_msg['message']['from']['first_name']
# 	last_chat=last_msg['message']['text']
# 	return last_chat,personid,personName
# # a,b = retrieve_LastMessage()
# # print(a)
# while True:
# 	chat,Userid,name = retrieve_LastMessage()

# 	print(chat,Userid,name)
# 	if "hello" in chat.lower() or "hi" in chat.lower():
# 		message = "Hello {}".format(name)
# 		res = bot_send_message(message, Userid)
# 		print("res")
# 		break
import requests
import json
from configparser import ConfigParser
from bs4 import BeautifulSoup
url = "https://api.telegram.org/bot"
def app_config_file(config):
		parser = ConfigParser()
		parser.read(config)
		return parser.get('Credential', 'token')
telegrambot = url + app_config_file('config.ini') 





def fetch_job():
	try:
		req = requests.get("https://www.indeed.co.in/jobs?q=python+developer&l=Pune,+Maharashtra&jt=fulltime&fromage=1").text
		soup = BeautifulSoup(req,'html.parser')
		alist=[]
		allJob_title = soup.find_all('a',class_="jobtitle turnstileLink")
		titles = [job.text.strip() for job in allJob_title]
		links = [job['href'] for job in allJob_title]
		companys = [job.text.strip() for job in soup.find_all('span',class_='company')]
		all_info = zip(titles,links,companys)
		for (t,l,c) in all_info:
			alist.append("{} : {}".format(t,c))
		return alist
	except Exception as a :
		print("Error detail " , a)
	
def request_bot(url):
	
	try:
		request = requests.get(url)
		response = request.json()
	except HttpError as http_response:
		print("Error occured : {}".format(http_response))
	except Exception as exp:
		print("Detail of exception : {}".format(exp))
	return response

def bot_info():

	info = request_bot(telegrambot+"/getme")
	return info


def bot_receive_msg():

	resp = request_bot(telegrambot+"/getUpdates?timeout=100")
	return resp

def bot_send_message(message,chat_id):
	url = "{}/sendMessage?timeout=100&chat_id={}&text={}".format(telegrambot,chat_id,message)
	Bot_response = request_bot(url)
	return Bot_response

def retrieve_LastMessage():

	msg = bot_receive_msg()
	if msg is not None:
		list_msgs= msg['result']
		len_list=len(list_msgs)
		last_msg= list_msgs[len_list-1]
		update_id = last_msg['update_id']
		
	return last_msg
# a,b = retrieve_LastMessage()
# print(a)
update = 0

last_update = retrieve_LastMessage()['update_id']

# message = fetch_job()
# print(message)
while True:
	
	last_msg= retrieve_LastMessage()
	Userid=last_msg['message']['from']['id']
	name=last_msg['message']['from']['first_name']
	chat=last_msg['message']['text']
	update_id = last_msg['update_id']
	
	if (last_update + update == update_id):
		print("yes")
		update = update+ 1
		if "hello" in chat.lower() or "hi" in chat.lower():
			message = "Hello {}".format(name)
			res = bot_send_message(message, Userid)
		if "getjob" in chat.lower():
			message = fetch_job()
			print(message)
			res = bot_send_message (message, Userid)



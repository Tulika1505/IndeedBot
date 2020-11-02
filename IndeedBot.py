import bot
import requests
from bs4 import BeautifulSoup

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


update = 0

last_update = bot.retrieve_LastMessage()['update_id']

# message = fetch_job()
# print(message)
while True:
	
	last_msg= bot.retrieve_LastMessage()
	Userid=last_msg['message']['from']['id']
	name=last_msg['message']['from']['first_name']
	chat=last_msg['message']['text']
	update_id = last_msg['update_id']
	
	if (last_update + update == update_id):
		update = update+ 1
		if "hello" in chat.lower() or "hi" in chat.lower():
			message = "Hello {}".format(name)
			res = bot.bot_send_message(message, Userid)
		if "getjob" in chat.lower():
			message = fetch_job()
			res = bot.bot_send_message (message, Userid)


from bot import telegram_bot 

update_id = None

def make_reply(message):
	if message is not None:
		reply = "Hi"
	return reply

while True:
	updates = telegram_bot.get_updates(offset=None)
	updates = updates['result']
	if updates:
		for item in updates:
			update_id = item['update_id']
			try:
				message = item['message']["text"]
			except:
				message = None
			PersonId= item['message']['from']['id']
			reply = make_reply(message)
			telegram_bot.send_message(PersonId, message)
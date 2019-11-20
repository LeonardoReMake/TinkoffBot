import telebot

bot = telebot.TeleBot('1034082652:AAHA0W9lSDQeW4HQMnRHx8nBSoK6ZGdNFWM')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	print(message.from_user.id)

bot.polling(none_stop=True, interval=0)

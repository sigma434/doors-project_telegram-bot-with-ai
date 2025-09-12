import telebot

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7817058953:AAHE8Goy-3RBC99C9Q3jsegvBWh2dCBtux8")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if not message.photo:
        bot.reply_to(message, 'дай фото бро')
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = recognize(file_name)
    bot.reply_to(message, result)


bot.polling()

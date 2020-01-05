import telebot
import logging

'''
Creating a connection through proxy
'cause telegram is banned in my region <3
'''
# apihelper.proxy = {'https': 'socks5://127.0.0.1:9050'}
bot = telebot.TeleBot("884413936:AAHJlaDMhdifXoTB7LBQ-bV2RD2PXvZNczM")

'''
1. Creating a unique id dictionary for checking chat state;
2. Creating a unique message dictionary for truly task completing
'''
uniq_message = {}
st = False


@bot.message_handler(content_types=["text"])
def main_func(message):
    send_welcome(message)
    if "/help" in uniq_message[message.from_user.id] \
            and "/start" in uniq_message[message.from_user.id] \
            and "/document_rar" not in uniq_message[message.from_user.id]:
        eval_state(message)

    if "/document_rar" in uniq_message[message.from_user.id] and message.text == "eval()":
        ev_checker(message)

    if "/eval" in uniq_message[message.from_user.id]:
        give_flag(message)

    if "/flag_txt" in uniq_message[message.from_user.id]:
        flag_checker(message)


@bot.message_handler(commands=["start", "help", "commands"])
def send_welcome(message):
    global st

    if (message.from_user.id not in uniq_message.keys()):
        uniq_message[message.from_user.id] = []

    if ("/start" not in uniq_message[message.from_user.id] and message.text == "/start"):
        bot.reply_to(message, '''\n
        New release version is here.
        \nTask #1 : One of us. 
        \nFlag format: RFlag{...}
        \n List of available commands:
        \n/commands.''')
        photo = open(r'C:\Users\Riven\Desktop\one of us.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        st = True
        uniq_message[message.from_user.id] = ["/start"]
    print(uniq_message)

    if (st):
        if "/commands" not in uniq_message[message.from_user.id] and message.text == "/commands":
            bot.reply_to(message, "List of commands:\n"
                                  "/help. That's all :)")
            uniq_message[message.from_user.id].append("/commands")

        if "/help" not in uniq_message[message.from_user.id] and message.text == "/help" \
                and "/commands" in uniq_message[message.from_user.id]:
            bot.reply_to(message, "The scouts conveyed the message, but it seems that it is a little distorted: " 
                                  "It’s not enough to think like a RmxhZw==, you need to 6265636f6d65 a RmxhZw==."
                                  "\nTo check state : /state")
            uniq_message[message.from_user.id].append("/help")
            print(uniq_message)


@bot.message_handler(commands=['state'])
def eval_state(message):
    if (message.text == "/state"
            and "Flag" in str(bot.get_chat_member(message.chat.id, message.from_user.id))):
        bot.send_message(message.chat.id, "State : FL4G?")
        file_sender(message)
    elif (message.text == "/state" and "Flag" not in str(bot.get_chat_member(message.chat.id, message.from_user.id))):
        bot.send_message(message.chat.id, "State : None")


@bot.message_handler(content_types=['text'])
def file_sender(message):
    try:
        if ("/help" in uniq_message[message.from_user.id] and message.from_user.id in uniq_message.keys()
                and "/document_rar" not in uniq_message[message.from_user.id]):
            uniq_message[message.from_user.id].append("/document_rar")
            doc = open(r'C:\Users\Riven\Desktop\Новая папка.rar', 'rb')
            bot.send_document(message.chat.id, doc)
            bot.send_message(message.chat.id, "Insert function to continue: ")
            print(uniq_message)
    except Exception:
        pass


@bot.message_handler(content_types=['text'])
def ev_checker(message):
    if "/eval" not in uniq_message[message.from_user.id] and "/document_rar" in uniq_message[message.from_user.id]:
        if message.text == "eval()":
            uniq_message[message.from_user.id].append("/eval")
            bot.send_message(message.chat.id, '''
            @bot.message_handler(content_types=['text'])
            def flag(message):
                message.text = filtr(message)
                (eval(message.text))
                # To the developer:
                # Do not forget to change variable 'flag' to function!
                # And bot name from 'bot' to something another!
            ''')


@bot.message_handler(content_types=['text'])
def give_flag(message):
    if (message.text == "bot.send_message(message.chat.id, flag)" or message.text == "bot.send_message(message.chat.id,flag)"
    or "bot.send_message(chat_id=message.chat.id, text=flag)" in message.text
            and "/eval" in uniq_message[message.from_user.id]
            and "/flag_txt" not in uniq_message[message.from_user.id]):
        bot.send_message(message.chat.id, "VzBXX1kwVV80UjNfUjM0TExZXzZSMzRUX0g0Q3w8M1I=")
        uniq_message[message.from_user.id].append("/flag_txt")


@bot.message_handler(content_types=['text'])
def flag_checker(message):
    if message.text == "RFlag{W0W_Y0U_4R3_R34LLY_6R34T_H4C|<3R}" and "/flag_txt" in uniq_message[message.from_user.id] \
            and "/RFlag" not in uniq_message[message.from_user.id]:
        uniq_message[message.from_user.id].append("/RFlag")
        bot.send_message(message.chat.id, "Congtats! Thanks for doing this task!")
        bot.send_message(message.chat.id, '''\nIf you want to comment something, please\n
                                            contact to me:\n
                                            https://t.me/rive_n\n
                                            @rive_n\n
                                            https://t.me/rivens_basics\n
                                            @rivens_basics''')


logger = telebot.logger
telebot.logger.setLevel(level=logging.INFO)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    logger.info(call)


bot.polling(none_stop=True, interval=0)

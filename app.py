from data import dp, bot
from handlers import send_echo

dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)

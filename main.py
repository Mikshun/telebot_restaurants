import database.orm
from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter

if __name__ == '__main__':
    database.create_table()
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()

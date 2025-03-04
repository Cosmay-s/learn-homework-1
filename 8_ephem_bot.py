"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import give_token as t


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(t(), use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь!\nИспользуй команду: /planet <Название планеты> на английском языке\nНапример: /planet Mars')


def talk_to_me(update, context):
    user_text = update.message.text.split()
    planet_name = user_text[-1].capitalize()
    if planet_name == "Mars":
       planet = ephem.Mars()

    elif planet_name == "Venus":
         planet = ephem.Venus()

    elif planet_name == "Jupiter":
         planet = ephem.Jupiter()

    elif planet_name == "Saturn":
         planet = ephem.Saturn()

    elif planet_name == "Mercury":
         planet = ephem.Mercury()

    elif planet_name == "Uranus":
         planet = ephem.Uranus()

    elif planet_name == "Neptune":
         planet = ephem.Neptune()

    elif planet_name == "Earth":
         planet = ephem.Earth()

    elif planet_name == "Moon":
         planet = ephem.Moon()
         
    else:
        return update.message.reply_text(f"Планета {planet_name} не найдена. Попробуй еще раз.")
    planet.compute(ephem.now())
    constellation = ephem.constellation(planet)
    answer = f"Планета {planet_name} находится в созвездии: {constellation[1]}."
    update.message.reply_text(answer)


if __name__ == "__main__":
    main()

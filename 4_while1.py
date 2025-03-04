"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    user_answer = input("Как дела? ")
    while user_answer.lower() != 'хорошо':
        print('Это не то что я хочу услышать!')
        user_answer = input("Как дела? ")
    print('Хорошо что хорошо!')


    
if __name__ == "__main__":
    hello_user()

"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            user_answer = input("Как дела? ")
            if user_answer.lower() == 'хорошо':
                print("Хорошо что хорошо!")
                break
            else:
                print("Это не то что я хочу услышать!")
        except KeyboardInterrupt:
            print("\nПока!") 
            break 

if __name__ == "__main__":
    hello_user()



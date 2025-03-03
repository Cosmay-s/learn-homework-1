"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def check_two_words(first_word, second_word):
    try:

        if first_word == second_word:
            return 1
        
        if first_word != second_word and len(first_word) > len(second_word):
            return 2
        
        if first_word != second_word and second_word == "learn":
            return 3

    except(ValueError, TypeError):
        return 0
      
    

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_two_words(1, 'word'))
    print(check_two_words(1, 'learn'))
    print(check_two_words('word', 'word'))
    print(check_two_words('world', 'word'))
    print(check_two_words('word', 'learn'))
if __name__ == "__main__":
    main()

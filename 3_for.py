"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sales_data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def sum_for_product(data):
    for i in range(len(data)):
        product = data[i]['product']
        sum_sales = sum(data[i]['items_sold'])
        print(f'Суммарное количество продаж для {product} составляет {sum_sales} ед.')


def average_for_product(data):    
    for i in range(len(data)):
        product = data[i]['product']
        average_sales = sum(data[i]['items_sold']) / len(data[i]['items_sold'])
        print(f'Среднее количество продаж для {product} составляет {average_sales:.2f} ед.') 


def total_sum_for_product(data):
    total_sum = 0
    for i in range(len(data)):
      total_sum += sum(data[i]['items_sold'])
    return total_sum


def total_average_for_product(data):
    total_average = 0
    for i in range(len(data)):
      total_average += sum(data[i]['items_sold']) / len(data[i]['items_sold'])
    return total_average


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print('------------------------------------------------------------------------')
    sum_for_product(sales_data)
    print('------------------------------------------------------------------------')
    average_for_product(sales_data)
    print('------------------------------------------------------------------------')
    print(f'Суммарное количество продаж всех товаров {total_sum_for_product(sales_data)} ед.')
    print('------------------------------------------------------------------------')
    print(f'Cреднее количество продаж всех товаров {total_average_for_product(sales_data)} ед.')
    print('------------------------------------------------------------------------')
    

if __name__ == "__main__":
    main()
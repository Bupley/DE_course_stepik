purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

#Общая выручка
def total_revenue(input):
    total_revenue = 0
    for purchase in input:
        revenue = float(purchase.get("price"))*int(purchase.get("quantity"))
        total_revenue = revenue + total_revenue
    return total_revenue

print(f'Общая выручка: {total_revenue(purchases)}')

#Список товаров по категориям
def items_by_category(input):
    result_dict = {}
    for purchase in input:
        k = purchase["category"]
        v = purchase["item"]
        if k in result_dict:
            result_dict[k].append(v)
        else:
            result_dict[k] = [v]
    return result_dict

print (f'Товары по категориям:{items_by_category(purchases)}')

#Список покупок, где цена превышает заданное значение
min_price = 1.8
def expensive_purchases(input, min_price):
    exp_pur = []
    for purchase in input:
        if purchase["price"] >= min_price:
            exp_pur.append(purchase)
    return exp_pur

print(f'Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}')

#Средняя цена товаров по категориям
def average_price_by_category(input):
    result_dict = {}
    for purchase in input: #агрегация в словари категория-цены
        k = purchase["category"]
        v = purchase["price"]
        if k not in result_dict:
            result_dict[k] = [v]
        else:
            result_dict[k].append(v)
    for category in result_dict: #расчет среднего значения в каждом словаре
        count_of_items = len(result_dict[category])
        result_dict[category] = sum(map(float, result_dict[category]))/count_of_items
    return result_dict

print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')

#Категория с наибольшим числом проданных товаров
def most_frequent_category(input):
    result_dict = {}
    for purchase in input: #агрегация в словари категория-количества
        k = purchase["category"]
        v = purchase["quantity"]
        if k in result_dict:
            result_dict[k].append(v)
        else:
            result_dict[k] = [v]
    for category in result_dict: #расчет суммарного количества по каждой категории
        result_dict[category] = sum(map(int, result_dict[category]))
    max_q = 0
    max_cat = str()
    for category in result_dict: #поиск  наибольшего количества
        if result_dict[category] > max_q:
            max_q = result_dict[category]
            max_cat = category
    return max_cat

print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')

import pprint


def cook_book():
    with open("D:\\recipes.txt", encoding="utf-8") as file:
        file = file.read().split("\n")
        menu_dict = {}
        dish = ''
        for dishes in file:
            if dishes.isdigit():
                continue
            elif dish == dishes:
                continue
            elif "|" in dishes:
                ingredient_name = dishes.split("|")[0]
                quantity = int(dishes.split("|")[1])
                measure = dishes.split("|")[2]
                menu_dict[dish].append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            elif dishes == '':
                continue
            else:
                dish = dishes
                menu_dict[dishes] = []
        return menu_dict

#pprint.pprint(cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book1 = cook_book()
    for dish in dishes:
        for ingredient in cook_book1[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return dict(shop_list.items())


pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

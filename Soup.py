ingridients = {'Капуста': 'Щи', 'Свекла': 'Борщ', 'Колбаса': 'Солянка', 'Грибы': 'Грибной суп', 'Рыба': 'Уха', 'Без добавок': 'КИПЯТОК'}


def show_my_soup(ingridient):
    print(f'Ваш суп - {ingridients[ingridient]}')


class Soup:
    pass


for prod in ingridients.keys():
    print(prod)
while True:
    choice = input('Выберите ингридиент: ').capitalize()
    temp = []
    for prod in ingridients.keys():
        temp.append(prod)
    res = choice in temp
    if not res:
        print('Введите верный ингридиент')
    else:
        break
my_soup = Soup()
show_my_soup(choice)
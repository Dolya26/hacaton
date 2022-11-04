import json

FILE_PATH = '/home/doolot/Desktop/ev.25/files/CRUD/CRUD.json'
ID_FILEPATH = 'id.txt'

def get_data():
    with open(FILE_PATH) as file:
            return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)

# CRUD
def list_of_products():
    data = get_data()
    return f'Список всех товаров: {data}'

def detail_product():
    data = get_data()
    try:
        id = int(input('Введите ID продукта: '))
        product = list(filter(lambda x: id == x ['id'], data))
        return product[0]
    except:
        return 'Неправильное ID!'
    


def get_id():
    with open(ID_FILEPATH, 'r') as file:
        id = int(file.read())
        id +=1
    with open(ID_FILEPATH,'w') as file:
        file.write(str(id))
    return id

def craete_product():
    data = get_data()
    try:
        product = {
            'id': get_id(),
            'marka': input('Введите марку ноутбука: '),
            'model': input('Введите модель ноутбука: '),
            'vipusk': int(input('Введите год выпуска: ')),
            'opisanie': input('Добавьте описание: '),
            'price': round(float(input('Введите цену: ')), 2)
        }
    except Exception as e:
        print(e)
        return 'Неверные данные!'
    data.append(product)
    save_data(data)
    return 'Создан новый товар!'

def update_product():
    data = get_data()
    try:
        id = int(input('Введите ID продукта: '))
        product = list(filter(lambda x : x['id'] == id, data))[0]
        print(f'Продукт для обновления {product["title"]} ')
    except:
        return 'Неправильное ID!'


    index = data.index(product)
    choise = input('Что ты хочешь поменять? (1-title),(2-price),(3-description): ')
    if choise.lower().strip() == '1':
        data[index]['title'] = input('Введите новое название: ')
    elif choise.strip() == '2':
        try:
            data[index]['price'] = float(input('Введите новую цену: '))
        except:
            return 'Неправильная цена!'
    elif choise.strip() == '3':
        data[index]['description'] = input('Введите новое описание: ')
    else:
        return 'Неправильное значения для обновления!'

    save_data(data)
    return 'Новые значения сохранены ;)'


def delete_product():
    data = get_data()
    try:
        id = int(input('Введите ID продукта: '))
        product = list(filter(lambda x: x ['id'] == id, data))[0]
        print(f'Stagg for delete {product["title"]}')
    except:
        return 'Неправильное ID!'
    choise = input('Are you sure? yes/no?')
    if choise.lower().strip() != 'yes':
        return "Ok ;)"
    data.remove(product)
    save_data(data)
    return 'Успешно удалено :)'
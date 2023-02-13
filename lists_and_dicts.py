# Списки
lst = [3, 5, 7, 9, 10.5]
print(*lst)
lst.append('Python')
print(f'Список состоит из {len(lst)} элементов')

print(f'Начальный элемент списка: {lst[0]}')
print(f'Последний элемент списка: {lst[-1]}')
print('Элементы списка со второго по четвертый включительно:', *lst[1:4])
lst.remove('Python')
print('Окончательный список:', *lst)

# Словари
dct = {"city": "Москва", "temperature": "20"}
print(dct['city'])
dct['temperature'] = int(dct["temperature"]) - 5
print(dct)
print('Есть ли в словаре ключ country?', dct.get('country'))
print(dct.get('country', 'Россия'))
dct['data'] = '27.05.2019'
print('Длина словаря =', len(dct))

# Числа
a = 2
b = 0.5
print(a + b)
v = int(input('Введите число от 1 до 10: '))
ten = 10
print(v + ten)

# Строки
name = 'ДЕНИС'
print('Привет, {}!'.format(name.capitalize()))

name = input('Введите ваше имя: ')
print(f'Привет, {name.upper()}! Как дела?')


# Приведение типов
print(float('1'))
try:
    int('2.5')
except ValueError as error:
    print(error)

print(bool(1))
print(bool(''))
print(bool(0))

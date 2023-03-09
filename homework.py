# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

song = input()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
parts = song.split()
itog = list()
for item in parts:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    itog.append(k)
if len(set(itog)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
# Задание №2.
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и 
# столбцов таблицы, которые должны быть распечатаны
# . Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно 
# два аргумента, как, например, у операции умножения.
def print_operation_table(operation, num_rows=6, nu_columns=6):
    if operation(1,1)==2:
        print(1,end='\t')

    for row in range(1, num_rows+1):
        for column in range(1, nu_columns+1):
            if operation(1,1)==2:
                column=column-1
            print(operation(row,column), end='\t')
        print()

# Задача
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных
def readfile(filename):
    
    return open(filename).read().split('\n')
 
def scan(data):
    
    for i in  data:
        print(i)
        
def search(data):
    
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')
    
data = readfile('data.txt') 
dict_command = {'1' :  scan, '2' : search} 
 
print('''Команды для работы со справочником:
    Просмотр всех записей справочника:  - 1
    Поиск по справочнику -2
    Добавление новой записи - 3
    Удаление записи из справочника по Имени и Фамилии - 4
    Изменение любого поля в определенной записи справочника - 5 
    Вывод возраста человека (записи) по Имени и Фамилии - 6 ''')
 
while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')

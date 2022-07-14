# lab1

v_list = ['astr', 3, 4.5, [1, 2], {1, 2}, (1, 2), (-3 + 3j), False, TypeError, {6: 'rtr', 8: 'fdsfd'}]
# либо цикл по for i in range(len(v_list)):
for i, v in enumerate(v_list):
    print(f"Тип {i}-го элемента со значением {v} =", type(v))

# lab 2

v_list2 = []
n = int(input("введите размерность списка: "))

for i in range(n):
    v_list2.append(str(input("введите значения списка ")))
print(f"OLD list {v_list2}")
for j in range(1, n, 2):
    v_list2[j - 1], v_list2[j] = v_list2[j], v_list2[j - 1]
print(f"NEW list {v_list2}")

# lab3
list_12 = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
           'Декабрь']
dic_12 = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
          10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
dic_season = {'Winter': (1, 2, 12), 'Spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}
v_in = int(input("ВВедите номер месяца: "))
i = 0
while i == 0:
    if v_in > 12 or v_in < 1:
        print("ВВеденное число от 1 до 12, пробуйте еще раз")
        i = 0
        v_in = int(input("ВВедите номер месяца: "))
    else:
        i = 1
print(f"Сначала список.  Вы выбрали {list_12[v_in - 1]}")
print(f"Теперь словарик. Вы выбрали {dic_12.get(v_in)}")
for j in dic_season.keys():
    if v_in in dic_season.get(j):
        print(f"И это у нас {j}")

# lab4
lst = []
str1 = input('Enter string: ').split()
for i, item in enumerate(str1):
    print(i + 1, f"{item[:10]}")

# lab5
lst_n = [1, 3, 5, 7, 9, 44, 33, 12, 16, 45, 45, 66, 66, 77, 6]
v_input = int(input("Введите число: "))
j = 1
ins_index = 0
if v_input in lst_n:
    while True:
        if v_input == lst_n[lst_n.index(v_input) + j]:
            j += 1
        else:
            ins_index = lst_n.index(v_input) + j
            lst_n.insert(ins_index, v_input)
            break
else:
    lst_n.insert(0, v_input)
print(lst_n)

#lab6


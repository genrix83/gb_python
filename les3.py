# lab1
a = float(input("Число1 "))
b = float(input("Число2 "))


def func1(arg1, arg2):
    if arg2 == 0:
        print("На ноль делить нельзя")
        exit()
    else:
        v1 = arg1 / arg2
        return v1


print(func1(a, b))


# lab2
def pers(pname, psur, pbd, pcity, pemail, pphone):
    if len(pname) < 2 or psur.isdigit() or len(
            psur) < 2 or pname.isdigit():  # можно еще на дату проверку и т.п. можно отдельно функцию по проверке запустить
        print("bad")
    else:
        return pname + ' ' + psur + ' ' + pbd + ' ' + pcity + ' ' + pemail + ' ' + pphone


my_pers = pers(pname='Влад', psur='Ivanov', pcity='Piter', pphone='9270707', pemail='rr@yy.tt', pbd='01/01/91')
print(my_pers)


# lab3
def my_func(a, b, c):
    min_var = a
    if min_var > b:
        min_var = b
        s1 = a
    else:
        s1 = b
    if min_var > c:
        s2 = min_var
        min_var = c
    else:
        s2 = c
    print("SUM  =  ", s1 + s2)


a = float(input("Число1 "))
b = float(input("Число2 "))
c = float(input("Число3 "))
my_func(a, b, c)


# lab4
def m_func(a, b):
    i = 1
    res = a
    while i < b:
       res *= a
       i += 1
    print(res)
a = float(input("Число1 "))
b = float(input("Число2 "))
m_func(a, b)

#lab5
#total = 0
#while True:
#    v_in = input("Введите числа через пробел. $ для выхода  ").split(' ')
#    if '$' in v_in:
#        if len(v_in) >= 2:
#            total += sum(map(int, v_in[len(v_in)-2]))
#            print(total)
#            break
#    else:
#        total += sum(map(int,v_in))
#        print(total)

#lab6
def int_func(str_a):
    #print(str_a)
    print(str_a.title())


str_1 = input("Enter word ")
int_func(str_1)
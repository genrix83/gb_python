#lab1
input_v = int(input("Enter digit: "))
print(input_v, " and type is ", type(input_v))
input_v = str(input_v)
print("Now type of out_str is", type(input_v))

#lab2
input_sec = int(input("Please, enter seconds: "))
v_hours = input_sec // 3600
v_minutes = (input_sec % 3600) // 60
v_sec = input_sec % 60
print(f"You enter: {v_hours:02}:{v_minutes:02}:{v_sec:02}")

#lab3
input_n = input("Enter digit: ")
v_sum = int(input_n) + int(input_n + input_n) + int(input_n + input_n + input_n)
print("Sum = ", v_sum)

#lab4
dig = int(input("Введите целое число: "))
max_dig = 0

while dig > 0:
    v_dig  = dig % 10
    if v_dig > max_dig:
        max_dig = v_dig
    dig = dig // 10
print(f"MAX {max_dig}")




#lab5
revenue = float(input("Enter revenue:"))
costs = float(input("Enter costs:"))

if revenue > costs:
    print(f"Фирма работает в прибыль с рентабельностью {(revenue-costs)/revenue*100} %")
    num_emp = int(input("Введите численность компании "))
    print(f"Прибыль на каждого сотрудника составила {(revenue-costs)/num_emp}")
elif revenue < costs:
    print("Вы в минусе")
else:
    print("Вы сработали в ноль. Напрягитесь")

#lab6
start = float(input("Введите стартовое число: "))
goal = float(input("Введите цель: "))
goal_day = 1
if start <= 0 or goal <= 0:
    print("Введите корректные значения")
else:
while goal > start:
    goal_day += 1
    start += start * 0.1
print(f"Вы достигнете цели за {goal_day} дней")
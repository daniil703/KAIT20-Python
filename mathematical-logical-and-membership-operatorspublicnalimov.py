print ("1 ЗАДАНИЕ")
a = 5 
b = 55

a = b # Теперь a = 55
b = 5 # Теперь b = 5

print("a =", a)
print("b =", b)

x = 7
y = 3
z = 0
print ("2 ЗАДАНИЕ")
print("Сумма x и y:", x + y) 
print("Разность x и y:", x - y)
print("Произведение x и y:", x * y)
print("Деление x на y с остатком:", x % y)
print("Деление x на y без остатка:", x // y)
print("x в степени y:", x ** y)
z = x**2 - (x * y)
print("Значение z:", z)

print ("3 ЗАДАНИЕ")
m = 8
n = 4

m = m + n
print("Значение m после сложения:", m)

n = m * 2
print("Значение n после умножения на 2:", n)

m = n % m
print("Значение m после нахождения остатка:", m)

n = n - m
print("Знвачение после вычитания", n)

print("Итоговое значение m:", m)
print("Итоговое значение n:", n)

print ("4 ЗАДАНИЕ")
a = 12
b = 8
c = 12

print(a > b) # True
print(b < a) # True
print(b != c) # True
print(a >= c) # True
print(b <= a) # True

print ("5 ЗАДАНИЕ")

backpack = ["ручка", "тетрадь", "учебник", "карандаш", "фломастеры", "линейка", "ластик"]

if "карандаш" in backpack:
    print("В рюкзаке карандаш.")
else:
    print("В рюкзаке нет карандаша.")
if "яблоко" not in backpack:
    print("В рюкзаке нет яблока.")
else:
    print("В рюкзаке яблоко.")

print("Длина рюкзака:", len(backpack))

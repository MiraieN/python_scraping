print('Ви отримали лист із Хогвардсу і тепер готуєтеся до того, щоб поринути в світ магії та чудес. \nЗараз ви можете зазирнути в чанівну кулю і побачити майбутнє. \nВи готові?')
input()
a = b = c = d = 0


print('Уявіть приміщення, де вам комфортно знаходитись. Яке воно?\n1) велике\n2) маленьке')
n = int(input())
while n != 1 and n != 2:
    print('Прислухайтесь до себе та оберіть один варіант')
    n = int(input())
if n == 1:
    a += 1
    c += 1
    b += 1
elif n == 2:
    d += 1


print('Яке тут освітлення?\n1) штучне\n2) природне')
n1 = int(input())
while n1 != 1 and n1 != 2:
    print('Прислухайтесь до себе та оберіть один варіант')
    n1 = int(input())
if n1 == 1:
    a += 1
    d += 1
elif n1 == 2:
    c += 1
    b += 1


print('Чи багато в кімнаті дзеркал?\n1) так\n2) ні/немає')
n2 = int(input())
while n2 != 1 and n2 != 2:
    print('Прислухайтесь до себе та оберіть один варіант')
    n2 = int(input())
if n2 == 1:
    a += 1
    c += 1
elif n2 == 2:
    b += 1
    d += 1


print('У кутку ви бачите стіл. Що на ньому?\n1) скляна статуетка\n2) тарілка із фруктами та солодощами\n3) настільна гра\n4) запечатаний конверт ')
n3 = int(input())
while n3 != 1 and n3 != 2 and n3 != 3 and n3 != 4:
    print('Прислухайтесь до себе та оберіть один варіант')
    n3 = int(input())
if n3 == 1:
    b += 1
elif n3 == 2:
    d += 1
elif n3 == 3:
    c += 1
elif n3 == 4:
    a += 1


print('Біля стола стоїть велика скриня. З чого вона зроблена?\n1) дерево\n2) золото\n3) срібло\n4) кришталь')
n4 = int(input())
while n4 != 1 and n4 != 2 and n4 != 3 and n4 != 4:
    print('Прислухайтесь до себе та оберіть один варіант')
    n4 = int(input())
if n4 == 1:
    d += 1
elif n4 == 2:
    c += 1
elif n4 == 3:
    a += 1
elif n4 == 4:
    b += 1


print('Відкрийте цю скриню. Що в ній лежить?\n1) перо\n2) ніж\n3) пробірка із зіллям\n4) казан')
n5 = int(input())
while n5 != 1 and n5 != 2 and n5 != 3 and n5 != 4:
    print('Прислухайтесь до себе та оберіть один варіант')
    n5 = int(input())
if n5 == 1:
    b += 1
elif n5 == 2:
    c += 1
elif n5 == 3:
    a += 1
elif n5 == 4:
    d += 1

print('Ви виходите із цієї кімнати. Куди ви потрапили?\n1) непроглядний ліс\n2) беріг озера\n3) сад\n4) вершина гори')
n6 = int(input())
while n6 != 1 and n6 != 2 and n6 != 3 and n6 != 4:
    print('Прислухайтесь до себе та оберіть один варіант')
    n6 = int(input())
if n6 == 1:
    a += 1
elif n6 == 2:
    b += 1
elif n6 == 3:
    d += 1
elif n6 == 4:
    c += 1

if a > b and a > c and a > d:
    print ('СЛІЗЕРИН!')
elif b > a and b > c and b > d:
    print ('КОГТЕВРАН!')
elif c > a and c > b and c > d:
    print ('ГРИФИНДОР!')
elif d > a and d > c and d > b:
    print ('ХАФЛПАФ!')

# a - слізерин
# b - когтевран
# c - грифиндор
# d - хафлпаф

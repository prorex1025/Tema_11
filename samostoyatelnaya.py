# 1) Простой итератор
print("=== Простой итератор ===")
a = [i ** 2 for i in range(1, 5)]
print('a -', a)
for i in a:
    print(i)

# 2) Выражения-генераторы
print("\n=== Выражения-генераторы ===")
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:  # Не выведет ничего, так как генератор уже исчерпан
    print(i)

# 3) Генератор с yield
print("\n=== Генератор с yield ===")
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

counter = countdown(5)
for i in counter:
    print(i)
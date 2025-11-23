def fib(n):
    """
    Генератор чисел Фибоначчи
    """
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Вывод 200-го числа Фибоначчи
if __name__ == "__main__":
    # Находим 200-е число Фибоначчи
    fib_200 = None
    for i, num in enumerate(fib(200), 1):
        if i == 200:
            fib_200 = num
            break
    
    print(f"200-е число Фибоначчи: {fib_200}")
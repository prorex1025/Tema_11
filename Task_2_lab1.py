def fib_with_save(n, filename="fib.txt"):
    """
    Генератор чисел Фибоначчи с сохранением в файл
    """
    a, b = 1, 1
    count = 0
    
    # Очищаем файл перед записью
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("")
    
    while count < n:
        # Записываем число в файл
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{a}\n")
        
        yield a
        a, b = b, a + b
        count += 1

# Основная программа
if __name__ == "__main__":
    print("Генерация чисел Фибоначчи...")
    
    # Генерируем 200 чисел и сохраняем в файл
    fib_200 = None
    for i, num in enumerate(fib_with_save(200), 1):
        if i == 200:
            fib_200 = num
            break
    
    print(f"200-е число Фибоначчи: {fib_200}")
    print("Все числа записаны в файл 'fib.txt'")
    
    # Читаем и выводим первые 10 чисел из файла для проверки
    print("\nПервые 10 чисел из файла:")
    try:
        with open("fib.txt", 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if i <= 10:
                    print(f"{i}: {line.strip()}")
                else:
                    break
    except FileNotFoundError:
        print("Файл не найден")
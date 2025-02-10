def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск 1 з {source} на {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістити диск {n} з {source} на {target}")
    hanoi(n - 1, auxiliary, target, source)


# Кількість дисків
n = 3
# Виклик функції
hanoi(n, "A", "C", "B")

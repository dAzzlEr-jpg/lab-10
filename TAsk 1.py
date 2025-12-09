B = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

not_zero = [x for x in B if x != 0]
zero = [x for x in B if x == 0]

result = not_zero + zero

print("Результат:", result)

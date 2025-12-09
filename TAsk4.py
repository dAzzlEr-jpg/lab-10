import numpy as np

# 1. Задаю два масиви
array1 = np.array([10, 20, 35, 40])
array2 = np.array([5, 10, 15, 2])

print("--- Початкові дані ---")
print(f"Масив 1: {array1}")
print(f"Масив 2: {array2}")
print("-" * 30)

# 2. Виконання арифметичних операцій
print("--- Арифметичні операції ---")
print(f"Сума:      {array1 + array2}")
print(f"Різниця:    {array1 - array2}")
print(f"Множення:   {array1 * array2}")
print(f"Ділення:    {array1 / array2}")
print(f"Піднесення до степеня: {array1 ** 2}")
print("-" * 30)

# 3.Об'єднання масивів
combined_array = np.concatenate((array1, array2))

print("--- Операція конкатенації ---")
print(f"Об'єднаний масив: {combined_array}")
print("-" * 30)

# 4. Дії над масивами
print("--- Операції над об'єднаним масивом ---")
print(f"Максимальний елемент: {np.max(combined_array)}")
print(f"Мінімальний елемент: {np.min(combined_array)}")
print(f"Сума всіх елементів: {np.sum(combined_array)}")
print(f"Добуток усіх елементів: {np.prod(combined_array)}")
print("-" * 30)
def bubble_sort(nums):
   # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
   swapped = True
   while swapped:
       swapped = False
       for i in range(len(nums) - 1):
           if nums[i] > nums[i + 1]:
               # Меняем элементы
               nums[i], nums[i + 1] = nums[i + 1], nums[i]
               # Устанавливаем swapped в True для следующей итерации
               swapped = True

# Проверяем, что оно работает



def input_matrix():
   # Ввод размерности матрицы
   n = int(input("Введите количество строк (N): "))
   m = int(input("Введите количество столбцов (M): "))

   # Ввод элементов матрицы
   matrix = []
   print("Введите элементы матрицы построчно:")
   for i in range(n):
       row = list(map(int, input(f"Строка {i + 1}: ").split()))
       while len(row) != m:
           print(f"Ошибка! Введите {m} элемента(-ов).")
           row = list(map(int, input(f"Строка {i + 1}: ").split()))
       matrix.append(row)

   return matrix, n, m


def find_min_element(matrix):
   min_element = float('inf')  # Начальное значение для поиска минимума
   min_position = (-1, -1)  # Начальная позиция

   # Поиск минимального элемента и его индексов
   for i in range(len(matrix)):
       for j in range(len(matrix[i])):
           if matrix[i][j] < min_element:
               min_element = matrix[i][j]
               min_position = (i, j)

   return min_element, min_position


def main():
   matrix, n, m = input_matrix()

   # Находим минимальный элемент и его индексы
   min_element, (min_i, min_j) = find_min_element(matrix)

   # Вывод результата
   print("\nМатрица:")
   for row in matrix:
       print(row)
   random_list_of_nums = [5, 2, 1, 8, 4]
   bubble_sort(random_list_of_nums)
   print(f"\nМинимальный элемент: {min_element}")
   print(f"Индексы минимального элемента: ({min_i}, {min_j})")
   print('--------------------')
   print('Сортировка')
   print(random_list_of_nums)


if __name__ == "__main__":
   main()

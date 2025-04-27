recipes_count = int(input())
recipes = input().strip()

marks = [1]  # Первый рецепт имеет сложность 1

for recipe in recipes:
    if recipe == '+':
        marks.append(marks[-1] + 1)
    else:
        marks.append(marks[-1] - 1)

min_mark = min(marks)
max_mark = max(marks)

# Находим начальную сложность x
if min_mark >= 1:
    x = 1
else:
    x = 2 - min_mark  # x + min_mark - 1 >= 1 => x >= 2 - min_mark

# Корректируем сложности
adjusted_marks = [mark + (x - 1) for mark in marks]

# Находим номера самого простого и сложного рецептов
min_adjusted = min(adjusted_marks)
max_adjusted = max(adjusted_marks)

# Самый простой рецепт (первый с минимальной сложностью)
simplest = adjusted_marks.index(min_adjusted) + 1  # +1, так как нумерация с 1

# Самый сложный рецепт (последний с максимальной сложностью)
hardest = len(adjusted_marks) - 1 - adjusted_marks[::-1].index(max_adjusted) + 1

print(x)
print(simplest)
print(hardest)
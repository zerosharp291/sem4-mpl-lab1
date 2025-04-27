days_count = int(input())
notes = input().strip()

count_mastered = 0
current_recipe = 0
failures = [0] * (days_count + 2)  # Максимально возможное количество рецептов

i = 0
while i < days_count:
    if i < days_count - 1 and notes[i] == '+' and notes[i + 1] == '+':
        count_mastered += 1
        current_recipe += 1
        i += 2
    else:
        if notes[i] == '-':
            failures[current_recipe] += 1
        i += 1

max_failures = max(failures)
if max_failures == 0:
    print(count_mastered)
    print(-1, 0)
else:
    # Находим первый рецепт с максимальным количеством неудач
    first_max_recipe = failures.index(max_failures)
    print(count_mastered)
    print(first_max_recipe + 1, max_failures)  # +1, так как рецепты нумеруются с 1
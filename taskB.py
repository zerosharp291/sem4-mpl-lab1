n = int(input())
table = [] # данный список будет содержать информацию о рецепте внутри кортежа

for i in range(n):
    difficulty, desire = map(int, input().split())
    table.append((i + 1, difficulty - desire, difficulty, desire))

# сортировка
table.sort(key=lambda x: (-x[1], x[2], x[0])) # разница, сложность, индекс
print(table[-1][0])

#for i in table:
#    for j in i:
#        print(j, end=' ')
#    print()

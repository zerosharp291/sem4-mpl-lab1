from math import ceil

money_sum = 0
for i in range(3):
    salary, month = map(int, input().split())
    money_sum += salary / month

print(ceil(money_sum))

from math import floor
prices = [float(x) for x in input().split(",")]
expensive = max(prices)
while expensive in prices:
    prices.remove(expensive)
sum = 0
for each in prices:
    sum += (each * 0.3)
saved = sum + (sum * 0.07)
print(floor(saved))
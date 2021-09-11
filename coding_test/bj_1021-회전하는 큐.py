a = 1
d = 50
k = 50

result = 0

while d < 100:
    d *= (k * (d/100))
    result += a

print(result)
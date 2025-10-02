nums = list(range(1, 21))

result = list(map(lambda num: num**2  ,filter(lambda num: num%2==0 , nums)))

print(result)
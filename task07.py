

prices = ["$120", "$340", "$50", "$90"]

result = list(map(lambda pr: int(pr[1:]) , prices))

print(result)
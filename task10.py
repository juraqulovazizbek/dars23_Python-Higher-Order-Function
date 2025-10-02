text = ["apple", "34", "banana", "100", "abc", "75"]

result  = list(filter(lambda t: t.isdigit(), text))

print(result)
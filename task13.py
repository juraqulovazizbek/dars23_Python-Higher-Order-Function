sentence = "Functional programming in Python is very powerful and elegant"

suz = sentence.split()

result = sorted(suz, key=lambda sz: len(sz),reverse=True)[:3]

print(result)

people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

result = list(sorted(people , key = lambda p: p['age']))
print(result)
from pprint import pprint 

students = [
  {"name": "Azizbek", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

result = sorted(students, key=lambda st:st['grade'], reverse=False)
pprint(result)
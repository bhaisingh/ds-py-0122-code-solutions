person = {
    "first_name": "Rakesh",
    "last_name": "Singh",
    "hobby": "Coding"
}
print('person: ', person)
first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
print(first_name, last_name, middle_name)

person["Job"] = "Software Engineer"
print('Job: ', person["Job"])

person['hobby'] = "Fishing"
print('hobby: ', person['hobby'])

person.pop('last_name')
print('person: ', person)

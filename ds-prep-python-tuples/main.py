passenger = (12, True, "Bonnell, Miss. Elizabeth", "female", 58)
print('passenger: ', passenger)
name = passenger[2]
age = passenger[-1]
print('Name: ', name, 'Age: ', age)
survived_and_name = passenger[1:3]
gender_and_age = passenger[3:]
print('survived_and_name: ', survived_and_name, 'gender_and_age: ', gender_and_age)

is_female = "female" in passenger
is_male = "male" in passenger
print('is_female: ', is_female, 'is_male: ', is_male)

def get_survival_info(passenger):
    (id, survived, name, gender, age) = passenger
    return (age, gender, survived)

print('get_survival_info: ', get_survival_info(passenger))

value1 = (11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)
print('get_survival_info {0}: '.format(value1), get_survival_info(value1))
value2 = (28, False, "Fortune, Mr. Charles Alexander", "male", 19)
print('get_survival_info {0}: '.format(value2), get_survival_info(value2))
value3 = (51, False, "Panula, Master. Juha Niilo", "male", 7)
print('get_survival_info {0}: '.format(value3), get_survival_info(value3))
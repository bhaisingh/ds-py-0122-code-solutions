ages = [29, 19, 17, 26, 32, 16, 21]
print('ages: ', ages)
print('ages[4]: ', ages[4])
print('ages[-2]: ', ages[-2])
print('ages[2:6]: ', ages[2:6])
print('ages[:4]: ', ages[:4])

print('is 17 in ages?', 17 in ages)
print('is 42 in ages?', 42 in ages)

ages[2] = 18
print('ages: ', ages)

temp = ages[4]
ages[4] = ages[3]
ages[3] = temp
print('ages swap 4th <=> 5th : ', ages)

ages.append(45)
ages.insert(0, 32)
ages.insert(6, 37)
print('ages apend insert: ', ages)

ages.pop()
ages.pop(2)
print('ages pop: ', ages)


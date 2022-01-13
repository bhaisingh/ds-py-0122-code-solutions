record = (1, 'Grimdiana', 'Bones', 'boulders')
row = ''
for field in record:
    row += str(field) + ', '
print(row)

value_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for value in value_list:
    print(str(value))

index_list = []
for index in range(len(value_list)):
    index_list.insert(0,index)

print('index_list:', index_list)

for value in index_list:
    if value % 2 != 0:
        value_list.pop(value)

print('value_list:', value_list)

vowels={'A', 'E', 'I', 'O', 'U'}
parts_of_the_big_letter={'L', 'M', 'N', 'O', 'P'}

for vowel in vowels:
    if vowel in parts_of_the_big_letter:
        parts_of_the_big_letter.remove(vowel)

print('parts_of_the_big_letter:', parts_of_the_big_letter)

player_positions = {
    'Who': '1B',
    'What': '2B',
    "I Don't Know": '3B',
    "Why": "LF",
    "Because": "CF",
    "Tomorrow": "P",
    "Today": "C",
    "I Don't Care": "SS"
}

players = []
for keys in player_positions:
    players = players + [keys]
print('players:', players)

positions = {*()}
for position in player_positions.values():
  positions.add(position)

print('positions:', positions)

for key, value in player_positions.items():
  print(key + ' is on ' + value)

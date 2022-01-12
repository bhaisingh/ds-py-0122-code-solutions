record = (1, 'Grimdiana', 'Bones', 'boulders')
row = ''
for field in record:
    row += str(field) + ', '
print(row)

value_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for value in value_list:
    print(str(value) + '\n')

index_list = ''
for index in range(len(value_list)):
    print(index, value_list[index])

for value in value_list:
    if value % 2 != 0:
        value_list.remove(value)

print('value_list:', value_list)

vowels={'A', 'E', 'I', 'O', 'U'}
parts_of_the_big_letter={'L', 'M', 'N', 'O', 'P'}

for vowel in vowels:
    if vowel in parts_of_the_big_letter:
        parts_of_the_big_letter.remove(vowel)

print('parts_of_the_big_letter:', parts_of_the_big_letter)

player_positions = {
    "Who": "1B",
    "What": "2B",
    "I Don't Know": "3B",
    "Why": "LF",
    "Because": "CF",
    "Tomorrow": "P",
    "Today": "C",
    "I Don't Care": "SS"
}

players = ''
for keys in player_positions:
    players += keys + ': ' + player_positions[keys] + '\n'
print('players:', players)

positions = ''
for player in player_positions.values():
    positions += player + '\n'
print('positions:', positions)

for key, value in player_positions.items():
  print(key + ' is on ' + value)

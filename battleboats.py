from random import randint
from os import system
top_row = '''
            Battle Boats
    0  1  2  3  4  5  6  7  8  9
   -----------------------------'''
hit_marker = 'O'
miss_marker = 'X'
score = 0
total_attacks = 0
ship_coord_list = []
used_attack_coords = []
rows = []
updated_rows = []
ship_length_list = [2, 3, 4, 5]
list_pos_to_coord = {4:0, 7:1, 10:2, 13:3, 16:4, 19:5, 22:6, 25:7, 28:8, 31:9}
coord_to_list_pos = {0:4, 1:7, 2:10, 3:13, 4:16, 5:19, 6:22, 7:25, 8:28, 9:31}

def ship_spawn(ship_length, row, ship_y):
    og_ship_y = ship_y
    ship_x = randint(4, 21)
    if row[ship_x] == '.':
        direction = randint(0, 1000)
        for ship_unit in range(0, ship_length):
            ship_coord = str(list_pos_to_coord[ship_x]) + str(ship_y)
            ship_coord_list.append(ship_coord)
            if ship_coord_list.count(ship_coord) > 1:
                for extra_ship_coord in range(1, ship_unit + 1):
                    extra_ship_coord *= -1
                    del ship_coord_list[extra_ship_coord]
                break
            if direction % 2 == 0:
                ship_x += 3
            else:
                if ship_y < 9:
                    ship_y += 1
                else:
                    ship_y = og_ship_y - 1
        ship_length_list.remove(ship_length)
    return row

def update_board(marker, rows, attack_coords, total_attacks):
    attack_x = int((attack_coords)[0])
    attack_y = int((attack_coords)[1])
    updated_rows = []
    for row_position in range(0, len(rows)):
        row = rows[row_position]
        if row_position == attack_y:
            attack_x = coord_to_list_pos[attack_x]
            if row[attack_x] == '.':
                row_point_list = list(row)
                row_point_list.pop(attack_x)
                row_point_list.insert(attack_x, marker)
                row = ''.join(row_point_list)
        updated_rows.append(row)
    total_attacks += 1
    system('clear')
    print(top_row)
    print('\n'.join(updated_rows))
    print('HIT!') if marker == 'O' else print('MISS!')
    return updated_rows, total_attacks

for row_number in range(0, 10):
    rows.append(str(row_number) + '¦  .  .  .  .  .  .  .  .  .  .')

while len(ship_length_list) != 0:
    row_number = 0
    for row in rows:
        num = randint(0, 1000)
        if len(ship_length_list) == 0:
            break
        elif num % ship_length_list[0] == 0:
            row = ship_spawn(ship_length_list[0], row, row_number)
        row_number += 1
    if len(ship_length_list) != 0:
        ship_coord_list = []
        ship_length_list = [2, 3, 4, 5]
print(top_row)
print('\n'.join(rows))

while score != 14:
    try:
        attack_coords = input('Enter a coordinate XY:\n')
        if len(attack_coords) != 2:
            int('error')
        elif attack_coords in ship_coord_list and attack_coords not in used_attack_coords:
            used_attack_coords.append(attack_coords)
            rows, total_attacks = update_board(
                hit_marker, rows, attack_coords, total_attacks)
            score += 1
        elif attack_coords not in ship_coord_list and attack_coords not in used_attack_coords:
            used_attack_coords.append(attack_coords)
            rows, total_attacks = update_board(
                miss_marker, rows, attack_coords, total_attacks)
        elif attack_coords in used_attack_coords:
            int('error')
    except ValueError:
        system('clear')
        print(top_row)
        print('\n'.join(rows))
        print('PLEASE ENTER A 2 DIGIT INTEGER THAT YOU HAVE NOT ENTERED YET!')

newscore = 14 / total_attacks * 100
print('You Win! You had an accuracy of %.1f%%.' % (newscore))

import random

from game_logic import Game_Field
from game_logic import Create_Players

print('Игра в крестики нолики (3х3)')
# Создаем новое поле 3х3
field = Game_Field.Field(3, 3)
main_field = field.create_field()
# Просмотр поля
field.show_field(main_field)
# Создание игрока
player = Create_Players.Player(input('Введите Имя игрока: '))
print(f"Создан {str(player)}\n")


# Цикл игры до победы
def who_win():
    if main_field[0][0] == main_field[1][1] == main_field[2][2] != '.':
        return True
    if main_field[0][2] == main_field[1][1] == main_field[2][0] != '.':
        return True
    if main_field[0][0] == main_field[1][0] == main_field[2][0] != '.':
        return True
    if main_field[0][1] == main_field[1][1] == main_field[2][1] != '.':
        return True
    if main_field[0][2] == main_field[1][2] == main_field[2][2] != '.':
        return True
    if main_field[0][0] == main_field[0][1] == main_field[0][2] != '.':
        return True
    if main_field[1][0] == main_field[1][1] == main_field[1][2] != '.':
        return True
    if main_field[2][0] == main_field[2][1] == main_field[2][2] != '.':
        return True
    else:
        return False


while not who_win():
    try:
        # Ходы игрока
        print(f"\nХод игрока {player.name_player}")
        player_row = int(input('Введите номер строки: '))
        player_col = int(input('Введите номер столбца: '))
        while True:
            if main_field[player_row][player_col] == '.':
                main_field[player_row][player_col] = 'X'
                field.show_field(main_field)
                if who_win():
                    print(f'### {player.name_player} WINNER ###')
                    break
                else:
                    break
        if who_win():
            break
        # Ходы Компьютера
        print("\nХод Компьютера")
        cells = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        computer_choice = random.choice(cells)
        while True:
            if main_field[computer_choice[0]][computer_choice[1]] != '.':
                computer_choice = random.choice(cells)
            else:
                break
        while True:
            if main_field[computer_choice[0]][computer_choice[1]] == '.':
                main_field[computer_choice[0]][computer_choice[1]] = 'O'
                field.show_field(main_field)
                if who_win():
                    print('### COMPUTER WINNER ###')
                    break
                else:
                    break
        if who_win():
            break
    except Exception as ex:
        print(f'Не верно что-то ввели ({ex})')

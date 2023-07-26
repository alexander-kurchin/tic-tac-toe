def print_header() -> None:
    """ Вводит на экран заголовок """
    header = '''
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  _________   | || |     _____    | || |     ______   | |
| | |  _   _  |  | || |    |_   _|   | || |   .' ___  |  | |
| | |_/ | | \_|  | || |      | |     | || |  / .'   \_|  | |
| |     | |      | || |      | |     | || |  | |         | |
| |    _| |_     | || |     _| |_    | || |  \ `.___.'\  | |
| |   |_____|    | || |    |_____|   | || |   `._____.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  _________   | || |      __      | || |     ______   | |
| | |  _   _  |  | || |     /  \     | || |   .' ___  |  | |
| | |_/ | | \_|  | || |    / /\ \    | || |  / .'   \_|  | |
| |     | |      | || |   / ____ \   | || |  | |         | |
| |    _| |_     | || | _/ /    \ \_ | || |  \ `.___.'\  | |
| |   |_____|    | || ||____|  |____|| || |   `._____.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  _________   | || |     ____     | || |  _________   | |
| | |  _   _  |  | || |   .'    `.   | || | |_   ___  |  | |
| | |_/ | | \_|  | || |  /  .--.  \  | || |   | |_  \_|  | |
| |     | |      | || |  | |    | |  | || |   |  _|  _   | |
| |    _| |_     | || |  \  `--'  /  | || |  _| |___/ |  | |
| |   |_____|    | || |   `.____.'   | || | |_________|  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'                                                    
              Или «Крестики-нолики» по-русски.         

    '''
    print(header)


def input_players_names() -> dict:
    """ Сохраняет имена игроков в словарь """
    player_x = input('Игрок 1 (X) имя: ') or 'Игрок 1'
    player_0 = input('Игрок 2 (0) имя: ') or 'Игрок 2'
    return {'X': player_x, '0': player_0}


def show_field(field: list) -> None:
    """ Вводит на экран игровое поле"""
    print('\n')
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(field[0], field[1], field[2]))
    print('\t_____|_____|_____')
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(field[3], field[4], field[5]))
    print('\t_____|_____|_____')
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(field[6], field[7], field[8]))
    print('\t     |     |')
    print('\n')


def show_rules() -> None:
    """ Вводит на экран правила игры """
    rules = '''
    Поле состоит из девяти пронумерованных ячеек.
    Игроки по очереди вводят номер ячейки, которую хотят занять.
    Побеждает тот, кто сможет занять или всю строку, или весь столбец, или всю диагональ.
    '''
    print('\t' + 'П Р А В И Л А   И Г Р Ы' + '\n\n\n')
    field = [i for i in range(1, 10)]
    show_field(field)
    print('\n' + rules + '\n' * 10)


def check_win(field: list, current_player: str) -> bool:
    """ Проверяет, победил ли текущий игрок """
    # Все выигрышные комбинации
    winning_lines = ((0, 1, 2),
                     (3, 4, 5),
                     (6, 7, 8),
                     (0, 3, 6),
                     (1, 4, 7),
                     (2, 5, 8),
                     (0, 4, 8),
                     (2, 4, 6))
    # True, если совпала хоть одна
    return any([all([field[position] == current_player for position in line]) for line in winning_lines])


def start_game(players: dict) -> None:
    """ Сама игра """
    # Создаём новое поле и выводим его на экран
    field = [' ' for i in range(1, 10)]
    show_field(field)
    # Присваиваем стартовые значения
    current_player = 'X'
    step = 0
    # Начинается игра
    print('Да начнётся бой!\n\n\n')
    while True:
        # Игрок делает ход, выбирая номер ячейки
        try:
            # Приводим номер ячейки к её индексу в списке field
            move = int(input(f'{players[current_player]}, ваш ход: ')) - 1
            # Проверяем, что индекс в пределах диапазона [0..8]
            if move not in range(9):
                raise ValueError
            # Проверяем, что ячейка с данным индексом свободна
            if field[move] != ' ':
                raise ValueError
        # Исключение поднимается как при ошибке конвертации строки в число,
        # так и при провале дополнительных проверок
        except ValueError:
            # Сообщаем об ошибке ввода номера ячейки и сразу уходим на новую итерацию цикла
            print('Неверный номер ячейки, попробуйте ещё.')
            continue
        # Обновляем игровое поле и счётчик ходов
        field[move] = current_player
        show_field(field)
        step += 1
        # Проверям, победил ли текущий игрок после своего хода
        # Если да -- сообщаем имя победителя и прерываем цикл
        if check_win(field, current_player):
            print(f'Победил(а) {players[current_player]}!')
            break
        # Проверям, наступила ли ничья
        # Если да -- сообщаем об этом и прерываем цикл
        if step == 9:
            print('Ничья!')
            break
        # Смена текущего игрока
        current_player = '0' if current_player == 'X' else 'X'


def run() -> None:
    """ Основная функция """
    # Выводим заголовок
    print_header()
    # Пауза, чтобы не пришлось отматывать экран вверх
    input('Нажмите ENTER для продолжения...')
    print('\n' * 10)
    # Выводим правила игры
    show_rules()
    # Узнаём имена игроков
    players = input_players_names()
    # Стартуем игру
    start_game(players)
    # Прощаемся
    input('\n\n' + 'Это была хорошая игра.')


if __name__ == '__main__':
    run()

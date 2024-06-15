import random


def difficulty_selection():  # Выбор пользователем сложности
    print('Выберите сложность, для этого введите номер сложности:\n'
          '--------------------------------------------\n'
          '1 - очень легко(неограниченное число попыток)\n2 - легко(20 попыток)\n3 - нормально(10 попыток)\n'
          '4 - сложно(7 попыток)\n5 - невозможно(3 попытки)\n'
          '--------------------------------------------')
    difficult_level = 0
    while True:
        try:
            difficult_level = int(input('Ваш выбор: '))
            if not (1 <= difficult_level <= 5):
                print('Вы немного ошиблись, целое введите число от 1 до 5')
                continue
        except ValueError:
            print('Вы немного ошиблись, целое введите число от 1 до 5')
            continue
        break
    match difficult_level:
        case 1:
            return -1
        case 2:
            return 20
        case 3:
            return 10
        case 4:
            return 7
        case 5:
            return 3


def number_generator():  # Генерируем случайное число отвечающее требованиям задачи
    secret_number_str = ''
    for i in range(4):
        if i == 0:
            secret_number_str += str(random.randint(1, 9))
        else:
            while True:
                test_number = random.randint(0, 9)
                if str(test_number) not in secret_number_str:
                    secret_number_str += str(test_number)
                    break
    return secret_number_str


def taurus_check(input_number, random_number):  #функция проверки количества быков и коров
    bulls = 0
    cows = 0
    for i in range(4):
        if input_number[i] == random_number[i]:
            bulls += 1
        elif input_number[i] in random_number:
            cows += 1
    return f'bulls: {bulls}, cows: {cows}'


def different_numbers_check(check_number):  # функция проверки уникальности каждой цифры, возвращает True если есть
    numbers_list = list(str(check_number))  # повтор
    for i in range(len(numbers_list)):
        if numbers_list[i] in numbers_list[i + 1:]:
            return True
    return False


def player_inputs_check():  #Проверка правильности ввода
    while True:
        try:
            player_input = int(input('Введите четырехзначное число, с различными цифрами:\n'))
        except ValueError:
            print('Вы ввели не число')
            continue
        if not 1000 <= player_input <= 9999:
            print('Вы ввели не четырехчначное число')
            continue
        elif different_numbers_check(player_input):
            print('Не все цирфы уникальны в числе')
            continue
        return str(player_input)


def bulls_and_cows_game():
    print('\n--------------------------------------------')
    print('Добро пожаловать в игру "Быки и коровы"!\n Сделаем вид, что вы знаете правила, поэтому сразу к делу!')
    print('--------------------------------------------\n\n')
    difficult = difficulty_selection()
    games_number = number_generator()
    while difficult != 0:
        difficult -= 1
        player_input = player_inputs_check()
        print(taurus_check(player_input, games_number))
        if taurus_check(player_input, games_number) == f'bulls: 4, cows: 0':
            return f'Поздравляю загаданное число {games_number}'
    return f'Отличная попытка, но мы загадали число {games_number}, попробуйте уменьшить сложность и сыграть ещё раз'


print(bulls_and_cows_game())

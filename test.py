import random
number_one = int(input('Томонку диапазон: '))
number_two = int(input('Жогорку диапазон: '))

secret_number = random.randint(number_one, number_two)

count = 1
while True:
    number = int(input(f'{number_one} жана {number_two} ортосундагы санды табыныз: '))

    if number > secret_number:
        print('Сиз жазган сан чон')
    elif number < secret_number:
        print('Сиз жазган сан кичине')
    else:
        print(f'Куттуктайбыз сиз {secret_number} санын {count} иретте таптыныз')
        break
    count += 1

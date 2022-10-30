from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    damage = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return (f'{char_name} {damage} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {damage} {5 + randint(5, 10)}')
    elif char_class == 'healer':
        return (f'{char_name} {damage} {5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    elif char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    ability = 'применил специальное умение'
    if char_class == 'warrior':
        return (f'{char_name} {ability} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {ability} «Атака {5 + 40}»')
    elif char_class == 'healer':
        return (f'{char_name} {ability} «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    attacked = 'attack — чтобы атаковать противника'
    defenced = 'defence — чтобы блокировать атаку противника'
    specialed = 'special — чтобы использовать свою суперсилу'
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(f'Введи одну из команд: {attacked}, {defenced} или {specialed}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    choice_hero = 'Введи название персонажа, за которого хочешь играть'
    class_hero = 'Воитель — warrior, Маг — mage, Лекарь — healer'
    near_character = 'Сильный, выносливый и отважный'
    range_character = 'Обладает высоким интеллектом'
    heal_character = 'Черпает силы из природы, веры и духов'
    accept = 'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку'
    or_unaccept = 'чтобы выбрать другого персонажа'
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input(f'{choice_hero}: {class_hero}: ')
        if char_class == 'warrior':
            print(f'Воитель — дерзкий воин ближнего боя. {near_character}.')
        if char_class == 'mage':
            print(f'Маг — находчивый воин дальнего боя. {range_character}.')
        if char_class == 'healer':
            print(f'Лекарь — могущественный заклинатель. {heal_character}.')
        approve_choice = input(f'{accept}, {or_unaccept}').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))

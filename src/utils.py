from random import choice

from gallows import GALLOWS


def get_txt(filename: str) -> list:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.readlines()
        return data
    except FileNotFoundError:
        print(f"Файл не был найден.")
    except Exception as e:
        print(f"При чтении файла произошла ошибка: {str(e)}.")


def select_word(word_list: list) -> str:
    return choice(word_list).strip()


def get_input(guessed_letters: str) -> str:
    while True:
        player_input = input(f"Угадай букву: ").lower()
        if validate_input(player_input, guessed_letters):
            return player_input
        else:
            print(f"\nОшибка!"
                  f"\nВведи одну букву русского алфавита")
        

def validate_input(player_input: str, guessed_letters: str) -> bool:
     return (
        len(player_input) == 1
        and player_input in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        and player_input not in guessed_letters
    )


def get_guessed_letters(guessed_letters: str) -> str:
    return " ".join(sorted(guessed_letters))


def get_guessed_word(word: str, guessed_letters: str, attempts: int) -> str:
    current_letters = []
    for letter in word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")

    print(GALLOWS[6 - attempts])
    return " ".join(current_letters)


def hangman() -> None:
    attempts = 7
    file_words = get_txt('src/russian_nouns.txt')
    word = select_word(file_words)
    guessed_letters = set()
    guess_word = get_guessed_word(word, guessed_letters, attempts=0)

    while attempts > 0:
        print(f"Количество попыток: {attempts}")
        print("\n", "Использованные буквы: ", f"{get_guessed_letters(guessed_letters)}")
        print("\n", guess_word)
        guess = get_input(guessed_letters)

        if guess in word:
            print(f"\nВеликолепно!")
        else:
            print(f"\nПопробуйте еще раз(")
            attempts -= 1

        guessed_letters.add(guess)
        guess_word = get_guessed_word(word, guessed_letters, attempts)

        if all(letter in guessed_letters for letter in word):
            print(f"\nПоздравляю, Вы выиграли! Загаданное слово: ", word)
            return

    print(f"Вас повесили! Загаданное слово было: ", word)


def main() -> None:
    while True:
        print(f"\nДобро пожаловать в игру \'Виселица\'" 
              f"\nУ Вас будет 7 попыток, чтобы угадать слово"
              f"\nЕсли угадаете слово - Вы победили"
              f"\nЕсли попытки закончатся - Вы проиграли")
        game = input(f"\nХотите начать новую игру? Введите \'s\', чтобы продолжить"
                     f"\nВведите \'e\', чтобы выйти из игры\n").lower()
        
        if game == 's':
            hangman()
        elif game == 'e':
            print(f"Возвращайтесь поскорее, чтобы сыграть снова")
            return False

from class_word import Word
from picture import picture


class Game:
    _count_error = len(picture)

    def __init__(self):
        self._word = list(Word())
        self._len_word = len(self._word)
        self._used_chars = set()
        self._user_word = ''
        self._ast_list = ['*'] * self._len_word

        # GAME BEGIN
        self._start_game()

    def _start_game(self):
        print(f'The word is hidden {self._len_word} letters. [{self._show_ast_word()}]')

    def _show_ast_word(self):
        for idx, item in enumerate(self._word):
            if item in self._used_chars:
                self._ast_list[idx] = item

        return ''.join(self._ast_list)

    def run(self):
        user_error = 0

        while True:

            char = input(f'Enter the letter: ')[:1]

            if set(self._ast_list) == self._used_chars:
                print(f'You\'ve won! The word was {"".join(self._word)}')
                break

            if char in self._used_chars:
                print(f'This: "{char}" letter you have already entered.')
                continue

            if char.lower() in self._word:
                self._used_chars.add(char)
                print(f'Right! The letter "{char}" is in this word! The word now looks like {self._show_ast_word()}')
                continue

            print(picture[user_error])
            user_error += 1

            if user_error == self._count_error:
                print(f'Alas. You\'ve lost. :`(The hidden word was {"".join(self._word)}.')
                break


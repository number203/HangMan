from random import choice


class Word:
    list_words = ['hakkunamatata', 'internet', 'commodore', 'caterpillar']

    def __init__(self):
        self._word = choice(self.list_words)

    # For methods LEN, COUNT
    def __len__(self):
        return len(self._word)

    # For func LIST
    def __iter__(self):
        for _ in self._word:
            yield _

    # Returns random word from list
    def get(self) -> str:
        return self._word

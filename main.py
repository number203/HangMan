from class_game import Game


if __name__ == '__main__':

    while True:

        game = Game()

        game.run()

        if input('Again? (Y/N): ').upper() != 'Y':
            break

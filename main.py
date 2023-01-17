from class_game import Game


if __name__ == '__main__':

    while True:

        game = Game()

        game.run()

        if input('Сыграем еще раз? (Y/N): ').upper() != 'Y':
            break

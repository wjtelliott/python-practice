import pygame

class test():
    def __init__(self) -> None:
        print('Loading...')
    def run(self) -> None:
        print('Run')

if __name__ == '__main__':
    pygame.display.init()
    disp_size = (1280, 720)

    screen = pygame.display.set_mode(disp_size)
    pygame.display.set_caption('PyGame')

    game = test()
    game.run()

    # exit; close display, stop music
    pygame.quit()
    exit()

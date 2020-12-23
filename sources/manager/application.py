import pygame
import pygame_gui

from manager.constants import Options
from pygame_gui import UIManager
from pygame_gui.elements import UIButton
from layout.mainMenu import MainMenu

class App():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MineSweaper")

        self.iconImage = pygame.image.load('data/images/mine.png')
        pygame.display.set_icon(self.iconImage)

        self.options = Options()
        if self.options.fullscreen:
            self.window_surface = pygame.display.set_mode(self.options.resolution,
                                                          pygame.FULLSCREEN)
        else:
            self.window_surface = pygame.display.set_mode(self.options.resolution)

        self.background_surface = None

        self.ui_manager = UIManager(self.options.resolution, 'data/theme/mineSweaper_theme.json')

        self.clock = pygame.time.Clock()
        self.running = True

        '''
            Create game Window
        '''
        self.mainMenu = None


        self.recreate_ui()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.ui_manager.process_events(event)


    def recreate_ui(self):
        self.ui_manager.set_window_resolution(self.options.resolution)
        self.ui_manager.clear_and_reset()

        self.background_surface = pygame.Surface(self.options.resolution)
        self.background_surface.fill(self.ui_manager.get_theme().get_colour('dark_bg'))

        self.mainMenu = MainMenu(pygame.Rect((25, 25), (self.options.resolution[0] - 250, self.options.resolution[1] - 50)), self.ui_manager)

    def run(self):

        while self.running:
            time_delta = self.clock.tick() / 1000.0

            # check for input
            self.process_events()

            # respond to input
            self.ui_manager.update(time_delta)

            # draw graphics
            self.window_surface.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.window_surface)

            pygame.display.update()
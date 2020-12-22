import pygame
import pygame_gui

from manager.constants import Options
from pygame_gui import UIManager
from layout.mainMenu import MainMenu

class App():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Options UI")

        self.options = Options()
        if self.options.fullscreen:
            self.window_surface = pygame.display.set_mode(self.options.resolution,
                                                          pygame.FULLSCREEN)
        else:
            self.window_surface = pygame.display.set_mode(self.options.resolution)

        self.background_surface = None

        self.ui_manager = UIManager(self.options.resolution, 'data/theme/mineSweaper_theme.json')
        self.recreate_ui()
        self.clock = pygame.time.Clock()
        self.running = True

        '''
            Create game Window
        '''
        self.mainMenu = MainMenu(pygame.Rect((0, 0), self.options.resolution), self.ui_manager)

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

    def run(self):

        while self.running:
            time_delta = self.clock.tick() / 1000.0

            self.process_events()
            # check for input

            self.ui_manager.update(time_delta)



            # draw graphics
            self.window_surface.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.window_surface)

            self.mainMenu.update(time_delta)

            pygame.display.update()
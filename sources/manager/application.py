import pygame
import pygame_gui

from manager.constants import Options
from pygame_gui import UIManager

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

        self.ui_manager = UIManager(self.options.resolution, 'data/theme/theme_2.json')
        self.recreate_ui()
        self.clock = pygame.time.Clock()
        self.running = True


    def recreate_ui(self):
        self.ui_manager.set_window_resolution(self.options.resolution)
        self.ui_manager.clear_and_reset()

        self.background_surface = pygame.Surface(self.options.resolution)
        self.background_surface.fill(self.ui_manager.get_theme().get_colour('dark_bg'))

    def run(self):

        while self.running:
            time_delta = self.clock.tick() / 1000.0


            # check for input

            self.ui_manager.update(time_delta)



            # draw graphics
            self.window_surface.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.window_surface)

            pygame.display.update()
import pygame
import pygame_gui

from pygame_gui import UIManager
from manager.constants import Options
from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from pygame_gui.elements import UIHorizontalSlider

class MainMenu(UIWindow):
    def __init__(self, rect, ui_manager):
        super().__init__(rect, ui_manager,
                         window_display_title='Scale',
                         object_id='#main_menu',
                         resizable=True)

        self.options = Options()
        ui_window = self
        button_layout_rect = pygame.Rect(30, 20, 100, 40)
        self.disable_toggle = UIButton(relative_rect=button_layout_rect,
                                       text='Disable',
                                       manager=ui_manager,
                                       object_id='#disable_button',
                                       container=ui_window)
        button_layout_rect1 = pygame.Rect(30, 80, 100, 40)
        self.hide_toggle = UIButton(relative_rect=button_layout_rect1,
                                    text='Hide',
                                    manager=self.ui_manager,
                                    object_id='#hide_button',
                                    container=ui_window)

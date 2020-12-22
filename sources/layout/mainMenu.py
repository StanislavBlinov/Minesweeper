import pygame
import pygame_gui

from pygame_gui import UIManager
from manager.constants import Options
from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton

class MainMenu(UIWindow):
    def __init__(self, rect, ui_manager):
        super().__init__(rect, ui_manager,
                         window_display_title='Scale',
                         object_id='#main_menu',
                         resizable=False)

        self.options = Options()
        self.startBtn = UIButton(pygame.Rect((int(self.options.resolution[0] / 2),
                                                 int(self.options.resolution[1] * 0.90)),
                                                (100, 40)),
                                    '',
                                    self.ui_manager,
                                    tool_tip_text="<font face=fira_code color=normal_text size=2>"
                                                  "<b><u>Test Tool Tip</u></b>"
                                                  "<br><br>"
                                                  "A little <i>test</i> of the "
                                                  "<font color=#FFFFFF><b>tool tip</b></font>"
                                                  " functionality."
                                                  "<br><br>"
                                                  "Unleash the Kraken!"
                                                  "</font>",
                                    object_id='#startBtn')

    def update(self, time_delta):
        super().update(time_delta)
        self.startBtn.update(time_delta)
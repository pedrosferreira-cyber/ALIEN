import sys
import pygame

from settings import Settings
from ship import Ship
from bullet_manager import BulletManager
from fleet_manager import FleetManager
from game_events import GameEventHandler
from game_renderer import GameRenderer

class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color = self.settings.bg_color

        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship, FastAlien)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
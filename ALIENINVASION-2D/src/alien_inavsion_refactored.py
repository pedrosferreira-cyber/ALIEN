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
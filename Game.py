from GameInterface import GameInterface
from Enemy import Enemy
from Player import Player


interface = GameInterface
enemy = Enemy
player = Player

while(True):
    interface.game_interface()
    choose = input('> ')
    if (choose == "4"):
        print('You quite the game')
        break
from GameInterface import GameInterface
from Enemy import Enemy
from Player import Player


interface = GameInterface
enemy = Enemy()
player = Player()

while(True):
    interface.game_interface()
    choose = input('> ')
    if (choose == "4"):
        print('You quite the game')
        break
    elif (choose == "1"):
        player.set_stats(input('Enter your name: '), 50, 50, 100, 70)
        print(f'Welcome {player.get_name()}')
        interface.action_interface()
        choose = input('> ')
        
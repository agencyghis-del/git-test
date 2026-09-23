from GameInterface import GameInterface
from Enemy import Enemy
from Player import Player
import random


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
        if (choose == "6"):
            player.escape()
            break
        elif (choose == "1"):
            enemy.hp = interface.player_fight_sequence(player.attack, enemy.hp, enemy.defense)
            player.hp = interface.enemy_fight_sequence(enemy.attack, player.hp, player.defense)
            print(f"Your HP: {player.hp}")
            print(f"Enemy HP: {enemy.hp}")
            if not interface.hp_verification(player.hp, enemy.hp):
                break
        elif (choose == "2"):
            player.heal(random.randint(10, 30))
            print(f"Your HP: {player.hp}")
            player.hp = interface.enemy_fight_sequence(enemy.attack, player.hp, player.defense)
            print(f"Your HP: {player.hp}")
            if not interface.hp_verification(player.hp, enemy.hp):
                break
        elif (choose == "3"):
            enemy.attack = interface.shield_sequence(enemy.attack, player.defense)
            player.hp = interface.enemy_fight_sequence(enemy.attack, player.hp, player.defense)
            print(f"Your HP: {player.hp}")
            player.defense = player.defense - random.randint(5, 15)
            print(f"Your Defense: {player.defense}")
            if not interface.hp_verification(player.hp, enemy.hp):
                break
        elif (choose == "4"):
            player.attack = interface.boost_sequence(random.randint(5, 15), player.attack, enemy.hp)
            player.hp = interface.enemy_fight_sequence(enemy.attack, player.hp, player.defense)
            print(f"Your HP: {player.hp}")
            if not interface.hp_verification(player.hp, enemy.hp):
                break
        elif (choose == "5"):
            player.pass_turn()
            player.hp = interface.enemy_fight_sequence(enemy.attack, player.hp, player.defense)
            print(f"Your HP: {player.hp}")
            if not interface.hp_verification(player.hp, enemy.hp):
                break
        
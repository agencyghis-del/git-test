class GameInterface:
    
    def action_interface():
        print("########################################################")
        print("#########           DEFEAT THE ENEMY          ##########")
        print("########################################################")
        print("")
        print("Select an option")
        print("1. Strike the enemy")
        print("2. Use a heal magic")
        print("3. Pare the enemy attack")
        print("4. Use a boost energy")
        print("5. Pass your turn")
        print("6. Escape")
        print("########################################################")
        
        
    def game_interface():
        print("########################################################")
        print("#########           HEROS FIGHTERS           ###########")
        print("########################################################")
        print("")
        print("Select an option")
        print("1. Start a party")
        print("2. View classment")
        print("3. Options")
        print("4. Quit the game")
        print("")
        print("########################################################")
    
    def player_fight_sequence(playerhit, enemyhp, enemydefense):
        print(f"You hit the enemy for {playerhit} damage")
        print(f"Enemy Defense: {enemydefense}")
        enemyhp = enemyhp - (playerhit - enemydefense)
        print(f"Enemy HP: {enemyhp}")
        return enemyhp
    
    def enemy_fight_sequence(enemyhit, playerhp, playerdefense):
        print(f"The enemy hit you for {enemyhit} damage")
        print(f"Your Defense: {playerdefense}")
        playerhp = playerhp - (enemyhit - playerdefense)
        print(f"Your HP: {playerhp}")
        return playerhp
    def heal_sequence(playerhp, playerheal):
        print(f"You healed yourself for {playerheal} HP")
        playerhp = playerhp + playerheal
        print(f"Your HP: {playerhp}")
        return playerhp
    def shield_sequence(enemyhit, playerdefense):
        print(f"You shielded yourself from the enemy attack")
        print(f"Your Defense: {playerdefense}")
        enemyhit = enemyhit - playerdefense
        print(f"The enemy hit you for {enemyhit} damage")
        return enemyhit
    def boost_sequence(playerboost, playerattack, enemyhp):
        print(f"You boosted your attack by {playerboost}")
        playerattack = playerattack + playerboost
        print(f"Your Attack boosted is: {playerattack}")
        enemyhp = enemyhp - playerattack
        print(f"You hit the enemy for {playerattack} damage")
        return enemyhp
    def pass_turn_sequence():
        print("You passed your turn")
    def enemy_pass_turn_sequence():
        print("The enemy passed his turn")
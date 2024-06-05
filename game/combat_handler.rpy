init python:
    class CombatHandler:
        def __init__(self):
            self.player_turn = True
            self.combat_status_string = " "
            self.current_enemy = None

        def next_turn(self):
            self.player_turn = not self.player_turn
            self.combat_status_string = " "

        def apply_damage(self, dmg):
            # handle miss
            if dmg == 0:
                self.combat_status_string = "Miss!"
                self.next_turn()
            # on the player's turn, apply damage to the enemy
            elif player_turn:
                enemy.apply_damage(dmg)
            # on the enemy's turn, apply damage to the player
            else: 
                g.apply_damage(dmg)

        def set_enemy(self, enemy):
            self.current_enemy = enemy
        


        
        
    
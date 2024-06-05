init python:
    class CombatHandler:
        def __init__(self):
            self.player_turn = True
            self.combat_status_string = ""
            self.current_enemy = None

        def next_turn(self):
            self.player_turn = not self.player_turn

        def enemy_defeated(self):
            self.combat_status_string = "Your foe is vanquished!"
            self.player_turn = True
            self.current_enemy = None
        

        def apply_damage(self, dmg):
            # handle miss
            if self.player_turn:
                if dmg == 0:
                    self.combat_status_string = "Miss!"
                    self.current_enemy.attack()
                    self.next_turn()
                # on the player's turn, apply damage to the enemy
                else:
                    self.current_enemy.apply_damage(dmg)
                    self.combat_status_string = "You hit the enemy for " + str(dmg) + " damage!"

                    if self.current_enemy.hp <1:
                        self.enemy_defeated()
                    else: 
                        self.next_turn()
                        self.current_enemy.attack()
                    #TODO: when enemy dies, reset turn to player
                    # and set enemy to None
                # on the enemy's turn, apply damage to the player
            else: 
                self.combat_status_string = self.combat_status_string + "\nThe enemy strikes at you..."
                if dmg == 0:
                    self.combat_status_string = self.combat_status_string + "\nAnd misses!"
                    self.next_turn()
                else:
                    self.combat_status_string = self.combat_status_string + "\nand hits you for " + str(dmg) + " damage!"
                    g.apply_damage(dmg)
                    self.next_turn()

        def get_combat_status_string(self):
            return self.combat_status_string

        def set_enemy(self, enemy):
            self.current_enemy = enemy
        


        
        
    
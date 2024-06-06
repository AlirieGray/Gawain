init python:
    class CombatHandler:
        def __init__(self):
            self.player_turn = True
            self.combat_status_string = ""
            self.current_enemy = None

        def next_turn(self):
            self.player_turn = not self.player_turn

        def enemy_defeated(self):
            # TODO: reward depends on difficulty of enemy. reward stat on enemy class
            self.combat_status_string = "Your foe is vanquished!\n You receive +10 gold. Feel free to spend it all in one place."
            g.change_gold(10)
            self.player_turn = True
            self.current_enemy = None
            calendar.increment_day()
            calendar.set_next_jump()

        def gawain_defeated(self):
            self.combat_status_string = "You have been defeated, you must retreat!"
            self.player_turn = True
            self.current_enemy = None
            calendar.increment_day()
            calendar.set_next_jump()
    
        # TODO: if the enemy misses twice, it's not clear that you need to push the button again
        # need a way to pause in between hits...
        # maybe dice animation will fix this?
        # turn order is also NOT working :(
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
                    self.player_turn = True # TODO hack
                else:
                    self.combat_status_string = self.combat_status_string + "\nand hits you for " + str(dmg) + " damage!"
                    g.apply_damage(dmg)
                    self.player_turn = True # TODO hack

        def get_combat_status_string(self):
            return self.combat_status_string

        def set_enemy(self, enemy):
            self.current_enemy = enemy
        


        
        
    
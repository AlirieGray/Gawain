init python:
    class CombatHandler:
        def __init__(self):
            self.combat_status_string = ""
            self.current_enemy = None
            self.current_reward = 0

        def next_turn(self):
            self.player_turn = not self.player_turn

        def enemy_defeated(self):
            if fought_morgana:
                renpy.jump("won_morgana_battle")
            else:
                # TODO: reward depends on difficulty of enemy. reward stat on enemy class
                if self.current_reward != 0:
                    if g.luck_potion_active:
                        self.current_reward = self.current_reward + 5
                        g.luck_potion_active = False
                    self.combat_status_string = "Your foe is vanquished!\n You receive +" + str(self.current_reward) + " gold. Feel free to spend it all in one place."
                
                g.change_gold(self.current_reward) # TODO + bonus from potion...
                self.current_enemy = None
                calendar.increment_week()
                calendar.set_next_jump()

        def gawain_defeated(self):
            if fought_morgana:
                renpy.jump("lost_morgana_battle")
            elif boss_time:
                self.combat_status_string = "This foe is beyond you!"
                renpy.jump("lost_big_boss_battle")
                calendar.increment_week()
                self.current_enemy = None
            else:
                self.combat_status_string = "You have been defeated, you must retreat!"
                self.current_enemy = None
                calendar.increment_week()
                calendar.set_next_jump()

        def enemy_attack(self):
            dmg = self.current_enemy.attack()
            if fought_morgana:
                self.combat_status_string = "Morgana lashes out with her magic..."
            else:
                self.combat_status_string = "The beast strikes at you..."
            if dmg == 0:
                self.combat_status_string = self.combat_status_string + "\nAnd misses!"
            else:
                self.combat_status_string = self.combat_status_string + "\nand hits you for " + str(dmg) + " damage!"
                g.take_damage(dmg)
            if g.current_hp < 1:
                self.gawain_defeated()
    
        def gawain_attack(self, attack_type):
            if attack_type == "swordplay":
                self.combat_status_string = "You strike with your sword."
            elif attack_type == "archery":
                self.combat_status_string = "You loose an arrow at the beast."
            else:
                self.combat_status_string = "You lash out with your bare fists."
            
            dmg = g.attack(attack_type, self.current_enemy)
            if dmg == 0:
                self.combat_status_string = self.combat_status_string + "\nYou miss."
            else:
                self.combat_status_string = self.combat_status_string + "\nYou hit the enemy for " + str(dmg) + " damage!"
                self.current_enemy.take_damage(dmg)
            if self.current_enemy.hp < 1:
                self.enemy_defeated()

        def get_combat_status_string(self):
            return self.combat_status_string

        def set_enemy(self, enemy):
            self.current_enemy = enemy
            self.current_reward = enemy.reward
        


        
        
    
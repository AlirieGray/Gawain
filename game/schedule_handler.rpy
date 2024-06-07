# TODO: need a new way to prompt combat at the end of the month with the new system...
# jump next_jump instead of town in the script at the end of scenes?

init python:
    class Task:
        def __init__(self, name, calendar, character):
            self.name = name
            self.character = character

        # TODO
        def roll_for_gold(self, stat):
            gawain_stat = self.character.stats_dict[stat]
            return 10

        # TODO fix roll numbers, add modifier math to Character class
        # or to dice utils
        def roll_for_skill(self, stat):
            gawain_stat = self.character.stats_dict[stat]
            modifier = get_modifier(gawain_stat)
            return roll(3, modifier)

        def get_outcome(self):
            # default stats 
            # TODO: figure out stats for all activities
            # TODO: the default behavior NOT working, might have to go back to getting outcome first?
            # TODO: just do pop-up for one skill at a time, forget about "Next Day" and week passing?
            stats = ['charm', 'intuition']

            if self.name == 'Tavern':
                stats = ['charm', 'intuition']
            elif self.name == 'Wash':
                stats = ['mettle', 'swordplay']
            elif self.name == 'Inn':
                stats = ['intuition', 'swordplay']
            elif self.name == 'Haven':
                stats = ['archery', 'charm']
            elif self.name == 'Cottages':
                stats = ['archery', 'mettle']

            return [{
                'skill_gain': self.roll_for_skill(stats[0]),
                'gold_gain': self.roll_for_gold(stats[0]),
                'stat_name': stats[0]
            },
            {
                'skill_gain': self.roll_for_skill(stats[1]),
                'gold_gain': self.roll_for_gold(stats[1]),
                'stat_name': stats[1]
            }]

    # utility function 
    def ordinal(n):
        return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

    # TODO: refactor class methods into a nice order and add documentation strings w input and output
    class Calendar:
        def __init__(self):
            self.current_month = 0
            self.current_week = 1
            self.next_jump = 'go_to_town'
            self.activity_slots = ['*none selected*']

            self.scenes_played = {
                'tavern': [False, False],
                'wash': [False, False, False, False],
                'cat': [False, False, False, False, False],
                'inn': [False, False, False],
            }
            self.months_list = [
                'Fallow Month', 
                'Haymaking Month',
                'Weed Month',
                'Holy Month',
                "Hunter's Moon Month",
                'Blood Month',
                ]

        def get_current_week(self):
            return self.current_week

        def set_played(self, location, scene_number):
            self.scenes_played[location][scene_number] = True
            self.increment_week()

        def get_day_number(self):
            if self.current_week == 1:
                return ordinal(1)
            if self.current_week == 2:
                return ordinal(8)
            if self.current_week == 3:
                return ordinal(22)
            else:
                return ordinal(30)

        def get_current_month_name(self):
            return self.months_list[self.current_month]

        def increment_week(self):
            # reset current task and outcomes   
            if self.get_current_week() == 4:
                self.current_month += 1
                self.current_week = 1
            else:
                self.current_week += 1
            self.activity_slots =  ['*none selected*']

            self.set_next_jump()

        def add_activity(self, activity):

            self.activity_slots[0] = activity
            self.set_next_jump() # TODO redundant?
        
        # TODO: also depends on which activity selected
        # TODO: call this function when incrememting calendar
        # TODO: distinguish story events from task incrementing stats view
        # TODO: map out all story events cleanly and refactor the class (maybe just a simple dict)
        # combat should also be at end of 4th week of activities
        def set_next_jump(self, jump=None):
            if jump:
                self.next_jump = jump
                return
            if self.activity_slots[0] == 'Visit Tavern': 
                if not self.scenes_played['tavern'][0]:
                    self.next_jump = 'first_tavern_event'
                elif not self.scenes_played['tavern'][1]:
                    self.next_jump = 'second_tavern_event'
            elif self.activity_slots[0] == 'Visit Washing Well': 
                if not self.scenes_played['wash'][0]:
                    self.next_jump = 'first_wash_event'
                elif not self.scenes_played['wash'][1]:
                    self.next_jump = 'second_wash_event'
                elif not self.scenes_played['wash'][2]:
                    self.next_jump = 'third_wash_event'
                else:
                    self.next_jump = 'wash_no_event'
            elif self.activity_slots[0] == 'Hang out at the Inn':
                if not self.scenes_played['inn'][0]:
                    self.next_jump = 'first_inn_event'
                elif self.current_month == 4 and not self.scenes_played['inn'][1]:
                    self.next_jump = 'inn_hunters_moon'
                else:
                    self.next_jump = 'inn_no_event'
            elif self.activity_slots[0] == 'Check out Cat Haven':
                if not self.scenes_played['cat'][0]:
                    self.next_jump = 'first_cat_haven_event'
                elif not self.scenes_played['cat'][1]:
                    self.next_jump = 'second_cat_haven_event'
                elif not self.scenes_played['cat'][2]:
                    self.next_jump = 'third_cat_haven_event'
                else:
                    self.next_jump = 'cat_no_event'
            elif self.current_month == 0 and self.current_week == 4:
                self.next_jump = 'first_combat_time'      
            else: 
                self.next_jump = 'go_to_town'
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
            self.current_day = 1
            self.current_day_outcome = [{'stat_name': 'charm', 'skill_gain': 0, 'gold_gain': 0}, {'stat_name': 'intuition', 'skill_gain': 0, 'gold_gain': 0}]
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

        def get_day_number(self):
            if self.current_week == 1:
                return ordinal(self.current_day)
            if self.current_week == 2:
                return ordinal(7 + self.current_day)
            if self.current_week == 3:
                return ordinal(14 + self.current_day)
            else:
                return ordinal(21 + self.current_day)

        def get_current_month_name(self):
            return self.months_list[self.current_month]

        def increment_week(self):
            self.current_day = 1
            # reset current task and outcomes   
            if self.get_current_week() == 4:
                self.current_month += 1
                self.current_week = 1
            else:
                self.current_week += 1
            self.activity_slots =  ['*none selected*']
            self.current_day_outcome = [{'stat_name': 'mettle', 'skill_gain': 0, 'gold_gain': 0}, {'stat_name': 'swordplay', 'skill_gain': 0, 'gold_gain': 0}]

        # TODO reset for beginning of week
        # TODO Set jump??? 
        # TODO: this math is NOT working :( 
        def increment_day(self):
            # if it's the last day of the week, set the week back to Monday.
            # if it's also the end of the month, increment the month and set weeks back to 1
            # otherwise just increment the week
            if self.current_day == 7:
                self.increment_week()
                self.set_next_jump()
                return
            # if it's not the last day of the week, just increment the day and set the jump
            self.current_day += 1
            self.set_next_jump()

        def add_activity(self, activity):
            # TODO: implement second activity slot
            self.activity_slots[0] = activity
            self.set_next_jump() # TODO redundant?
            if activity == "Visit Tavern":
                self.current_day_outcome = [{'stat_name': 'charm', 'skill_gain': 0, 'gold_gain': 0}, {'stat_name': 'intuition', 'skill_gain': 0, 'gold_gain': 0}]

        # TODO: also depends on which activity selected
        # TODO: call this function when incrememting calendar
        # TODO: distinguish story events from task incrementing stats view
        # TODO: map out all story events cleanly and refactor the class (maybe just a simple dict)
        # combat should also be at end of 4th week of activities
        def set_next_jump(self, jump=None):
            if jump:
                self.next_jump = jump
                return
            if self.activity_slots[0] == 'Visit Tavern' and self.current_day < 3: 
                if not self.scenes_played['tavern'][0]:
                    self.next_jump = 'first_tavern_event'
                elif not self.scenes_played['second_tavern']:
                    self.next_jump = 'second_tavern_event'
            elif self.activity_slots[0] == 'Visit Washing Well' and self.current_day < 3: 
                if not self.scenes_played['wash'][0]:
                    self.next_jump = 'first_wash_event'
                elif not self.scenes_played['wash'][1]:
                    self.next_jump = 'second_wash_event'
                elif not self.scenes_played['wash'][2]:
                    self.next_jump = 'third_wash_event'
                else:
                    self.next_jump = 'wash_no_event'
            elif self.activity_slots[0] == 'Hang out at the Inn' and self.current_day < 3:
                if not self.scenes_played['inn'][0]:
                    self.next_jump = 'first_inn_event'
                elif self.current_month == 4 and not self.scenes_played['inn'][1]:
                    self.next_jump = 'inn_hunters_moon'
                else:
                    self.next_jump = 'inn_no_event'
            elif self.current_month == 0 and self.current_week == 4 and self.current_day > 5:
                self.next_jump = 'first_combat_time'
            elif self.current_day > 5:
                self.next_jump = 'go_to_town'
            else: 
                self.next_jump = 'tasks_only'

    def execute_day():
        # creates a task object (for each activity) to roll for skills and gold
        # and returns a list of 7 (days) with each roll results

        # TODO: refactor this
        if calendar.activity_slots[0] == "Visit Tavern":
            task = Task('Tavern', calendar, g)
            outcomes = task.get_outcome()
            calendar.current_day_outcome = outcomes
            for outcome in outcomes:
                g.change_stat(outcome['stat_name'], outcome['skill_gain'])
            calendar.increment_day()

        elif calendar.activity_slots[0] == "Visit Washing Well":
            task = Task('Wash', calendar, g)
            outcomes = task.get_outcome()
            calendar.current_day_outcome = outcomes
            for outcome in outcomes:
                g.change_stat(outcome['stat_name'], outcome['skill_gain'])
            calendar.increment_day()
            
        # TODO: testing click to increment day....
        # TODO update Gawain object's skill and gold
        # cal.increment_week()

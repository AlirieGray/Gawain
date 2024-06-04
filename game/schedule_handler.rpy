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
            return roll(6, modifier)

        def get_outcome(self):
            stat = 'charm' # TODO???

            return {
                'skill_gain': self.roll_for_skill(stat),
                'gold_gain': self.roll_for_gold(stat),
                'stat_name': stat
            }

        # returns a list of outcome dicts (keys: skill_gain and gold_gain)
        # def get_outcomes_for_week(self):
        #     outcomes = []
        #     for i in range(7):
        #         outcomes.append(self.get_outcome())
        #     return outcomes

    # TODO: refactor class methods into a nice order and add documentation strings w input and output
    class Calendar:
        def __init__(self):
            self.current_month = 0
            self.current_week = 1
            self.current_day = 1
            self.current_day_outcome = {'stat_name': 'mettle', 'skill_gain': 0, 'gold_gain': 0}
            self.next_jump = 'first_story_event'
            self.activity_slots = ['*none selected*', '*none selected*']
            self.scenes_played = {
                'first_story_event': False,
                'second_story_event': False,
            }
            self.months_list = [
                'Hearthcake Month', 
                'Hrethmonth', 
                'Easter Month', 
                'Three Milkings Month', 
                'Fallow Month', 
                'Second Summer Month',
                'Weed Month',
                'Holy Month',
                "Hunter's Moon Month",
                'Blood Month',
                'After Yule Month'
                ]

        def get_current_week(self):
            return self.current_week

        def set_played(self, scene):
            self.scenes_played[scene] = True

        def get_day_number(self):
            if self.current_week == 1:
                return self.current_day
            if self.current_week == 2:
                return 6 + self.current_day
            if self.current_week == 3:
                return 13 + self.current_day
            else:
                return 20 + self.current_day

        def get_current_month_name(self):
            return self.months_list[self.current_month]

        def increment_week(self):
            if self.get_current_week() == 4:
                self.current_month += 1
                self.current_week = 1
            else:
                self.current_week += 1
            self.activity_slots =  ['*none selected*', '*none selected*']

        # TODO reset for beginning of week
        # TODO Set jump??? 
        # TODO: 7th of 2nd of etc. string
        def increment_day(self):
            # if it's the last day of the week, set the week back to Monday.
            # if it's also the end of the month, increment the month and set weeks back to 1
            # otherwise just increment the week
            # clear current day outcome when going to the next week
            if self.current_day == 7:
                self.current_day = 1
                self.current_day_outcome = {'stat_name': 'mettle', 'skill_gain': 0, 'gold_gain': 0}
                if self.current_week == 4:
                    self.current_month += 1
                    self.current_week = 1
                else:
                    self.current_week += 1
                self.set_next_jump()
                return
            # if it's not the last day of the week, just increment the day and set the jump
            self.current_day += 1
            self.set_next_jump()
            


        def add_activity(self, activity):
            # TODO: player should be able to select which slot they are filling
            # TODO: implement second activity slot
            self.activity_slots[0] = activity

        # TODO: also depends on which activity selected
        # TODO: call this function when incrememting calendar
        # TODO: distinguish story events from task incrementing stats view
        # TODO: map out all story events cleanly and refactor the class (maybe just a simple dict)
        # TODO: end of month should jump back to lake
        def set_next_jump(self, jump=None):
            if jump:
                self.next_jump = jump
                return
            if self.current_month == 0 and self.current_week == 1 and not self.scenes_played['first_story_event']:
                self.next_jump = 'first_story_event'
                self.set_played('first_story_event')
            elif self.current_month == 0 and self.current_week == 2:
                self.next_jump = 'first_combat_time'
            elif self.current_month == 1 and self.current_week == 1:
                self.next_jump = 'second_story_event'
            elif self.current_day > 5:
                self.next_jump = 'go_to_town'
            else: 
                self.next_jump = 'tasks_only'


    def execute_day():
        # creates a task object (for each activity) to roll for skills and gold
        # and returns a list of 7 (days) with each roll results

        # TODO: first task and second task
        if calendar.activity_slots[0] == "Visit Tavern":
            first_task = Task('Tavern', calendar, g)
            first_outcome = first_task.get_outcome()
            calendar.current_day_outcome = first_outcome
            g.change_stat(first_outcome['stat_name'], first_outcome['skill_gain'])
            calendar.increment_day()
            
        # TODO: testing click to increment day....
        # TODO update Gawain object's skill and gold
        # cal.increment_week()



# start task
# check if there is a story event
# if so, play the dialog
# open task screen
# show: name of task, day #, skill bar increasing, gold increasing
# iterate through days, roll each time for gold and skill gain
# use colors to show extra good skill/gold gain or not so good
# top portion, task 1. bottom text task 2. 
# calculate gold based on skill (TODO next iteration?)
# use flaticon free icon to show time passing
# honor/piety scale(s) 
# use global calendar to increment date, show in top right
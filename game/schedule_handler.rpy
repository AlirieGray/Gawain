init python:
    class Task:
        def __init__(self, name, calendar, character):
            self.name = name
            self.character = character

        # TODO
        def roll_for_gold(self, stat):
            gawain_stat = self.character.stats_dict[stat]
            return 10

        # TODO
        def roll_for_skill(self, stat):
            gawain_stat = self.character.stats_dict[stat]
            return 15

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

    class Calendar:
        def __init__(self):
            self.current_month = 0
            self.current_week = 1
            self.current_day = 0
            self.current_day_outcome = {'stat_name': 'mettle', 'skill_gain': 0, 'gold_gain': 0}
            self.next_jump = 'first_story_event'
            self.activity_slots = ['*none selected*', '*none selected*']
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
        def increment_day(self):
            self.current_day += 1

        def add_activity(self, activity):
            # TODO: player should be able to select which slot they are filling
            # TODO: implement second activity slot
            self.activity_slots[0] = activity

        # TODO: also depends on which activity selected
        # TODO: call this function when incrememting calendar
        # TODO: distinguish story events from task incrementing stats view
        def set_next_jump(self):
            if self.current_month == 0 and self.current_week == 1:
                self.next_jump = 'first_story_event'
            elif self.current_month == 1 and self.current_week == 1:
                self.next_jump = 'second_story_event'
            else:
                self.next_jump = 'go_to_town'

        

    def execute_day(cal, gawain):
        # execute_week takes a calendar and a gawain
        # creates a task object (for each activity) to roll for skills and gold
        # and returns a list of 7 (days) with each roll results

        # TODO: first task and second task
        # if cal.activity_slots[0] == "Tavern":
        first_task = Task('Tavern', cal, gawain)
        first_outcome = first_task.get_outcome()
        cal.current_day_outcome = first_outcome
        gawain.change_stat(first_outcome['stat_name'], first_outcome['skill_gain'])
        cal.increment_day()
        if cal.current_day == 6:
            cal.increment_week()
            
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
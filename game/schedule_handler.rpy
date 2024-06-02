init python:
    class Calendar:
        def __init__(self):
            self.current_month = 0
            self.current_week = 1
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

        def add_activity(self, activity):
            # TODO: player should be able to select which slot they are filling
            self.activity_slots[0] = activity

        # TODO: also depends on which activity selected
        # TODO: call this function when incrememting calendar
        # TODO: distinguish story events from task incrementing stats view
        def set_next_jump(self):
            if self.current_month == 0 and self.current_week == 1:
                self.next_jump = "first_story_event"

            if self.current_month == 1 and self.current_week == 1:
                    self.next_jump = "second_story_event"


init python:
    def wait_for_character_creation(points_remaining):
        while(points_remaining > 0):
            renpy.pause(1)
        return


    def wait_for_activity_selection(ready):
        while(not ready):
            renpy.pause(1)
        return
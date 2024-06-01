init python:
    def wait_for_character_creation(points_remaining):
        while(points_remaining > 0):
            renpy.pause(1)
        return
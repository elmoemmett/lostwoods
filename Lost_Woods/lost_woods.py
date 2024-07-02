"""
Python Portfolio Project
Emmett Tomkinson
Completed Feb 24, 2023
ASCII art Triforce credit goes to this source:
https://stackoverflow.com/questions/69517111/need-to-print-triforce-using-recursion

Module Docstring:
Importing the 'start' and 'move rooms' modeuls from the functions package
The start funciton will print out the opening lines introducing the storyline.
The move_rooms function will begin the process of the user choosing which direction to go
"""

from game_pkg.functions import start, move_rooms


start()
while True:
    move_rooms()

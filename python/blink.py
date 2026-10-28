import os
import time

# Frame 1: The Open Eye (Made of text characters)
open_eye = """
      .---.
    /       \\

   |   (O)   |
    \\       /
      '---'
"""

# Frame 2: The Blinking/Closed Eye
closed_eye = """
      .---.
    /       \\

   |   ---   |
    \\       /
      '---'
"""

def clear_screen():
    # Clears the terminal screen for Windows, Mac, or Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# The infinite loop that creates the animation
while True:
    clear_screen()
    print(open_eye)
    time.sleep(2.0)  # Keep the eye open for 2 seconds
    
    clear_screen()
    print(closed_eye)
    time.sleep(0.15) # Blink quickly for a fraction of a second

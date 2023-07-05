#!/usr/bin/env python3

from pynput.keyboard import Key, KeyCode, Listener
import pyautogui
import time
from tqdm import tqdm

def read_txt(txt_path: str) -> list[str]:
    # Open the list of commands to type
    # Read each line and create a list with each command as an element
    # Make sure to clean the list before executing program. It should look like this:

    # /spawnitem 123456
    # /spawnitem 987654
    # /spawnitem 123456
    # /spawnitem 987654

    with open(txt_path, 'r') as f:
        commands = f.readlines()

    # Print to screen for debugging purposes
    print(commands)
    return commands

def type_commands(commands: list[str]) -> None:
    
    # Counter for keeping track of progress
    currentPosition = 1

    # Loop through all commands to type them in one-by-one
    for cmd in tqdm(commands):
        
        # Strip the command of it's new line character '\n'
        cmd = cmd.strip()

        # These times are for delaying the program so the game doesn't get confused
        # Time between opening dialogue and entering command
        preCmdDelay = 0.25

        # Time between executing command and restarting the loop
        postCmdDelay = 0.5

        # If you have to open a dialogue to type, uncomment this
        # Start with dialogue closed before running program
        pyautogui.press('enter')

        # Delay by preCmdDelay seconds so the game can register
        time.sleep(preCmdDelay)

        # Type in the full command
        pyautogui.typewrite(cmd)

        # Press enter to input the command to the game
        pyautogui.press('enter')

        # Output current position in the list and add one to it for next time
        currentPosition += 1

        # Delay by postCmdDelay seconds so the game can register
        time.sleep(postCmdDelay)

def on_press(key) -> bool:
    if key == KeyCode.from_char(buttonToStartAutotyping):
        commands = read_txt('./commandlist.txt')
        type_commands(commands)
        return False

if __name__ == '__main__':

    # Make sure this does not conflict with any keybinding in the game!
    global buttonToStartAutotyping
    buttonToStartAutotyping = 'o'

    # Beginning of program
    # Wait for user input to start typing
    with Listener(on_press=on_press) as listener:
        listener.join()

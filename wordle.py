# Informatics INFO-I 210 - Summer 2023

"""
Wordle Assistant
================

Assists a user while they are playing Wordle, e.g.:
https://wordlewebsite.com/wordle-unlimited
"""

import user_interface as ui
from data_handling import load_text
import random

from typing import Any, Hashable, Iterable, Optional

# Use your solutions from Practice Set 09
from user_interface import count
from user_interface import count_letters
from user_interface import guesses_to_str
from user_interface import gridify
from user_interface import make_bar
from user_interface import make_bar_tail
from user_interface import counts_to_hist
# __________________________________________________________


p_words=list(load_text("valid-wordle-words.txt"))

def your_guess() -> str:
    print("After entering 'Your Guess' and if you win,"+'\n' + "enter 'GGGGG' into 'Result' to exit program" + '\n')
    user_str=input("Your Guess [xxxxx]                       >").lower()
    user_wordle_color=input("Result [(G)reen, (Y)ellow, g(R)ay]       >").upper()
    if user_wordle_color == "GGGGG":
        print('\n'+"Congratulations! You solved Wordle!")
    print('-'*80)
    color_wordle=""
    
    return (user_str,user_wordle_color)

def green_l(guess:str,feedback:str):
    gree={}
    for i in range(5):
        if feedback[i] == 'G':
            gree[i]=guess[i]
    return gree

def yellow_l(guess:str,feedback:str):
    yell={}
    for i in range(5):
        if feedback[i] == 'Y':
            yell[i] = guess[i]

    return yell


def gray_l(guess:str,feedback:str):
    grays=set({})
  
    for i in range(5):
        if feedback[i] == 'R':
            grays.add(guess[i])

    return grays

def gray_test(words:str,gray_set:set)-> bool:
    for letters in gray_set:
        if letters in words:
            return False
    return True

def yellow_test(words:str,yellow_set:dict)->bool:
    y_index=list(yellow_set.keys())
    y_letters=list(yellow_set.values())
    for i,letters in enumerate(words):
        for num in y_index:
            if i == num:
                if yellow_set[num] == letters:
                    return False
            if yellow_set[num] not in words:
                return False
    return True

def green_test(words:str,green_set:dict)-> bool:
    for key, num in green_set.items():
        if words[key] != num:
            return False
    return True


        
def find_potential_words(words:list,guess:str, feedback:str):
    color_wordle=""
    for i in feedback:
        if i == 'R':
            color_wordle+='⚪'
        elif i == 'G':
            color_wordle+="🟢"
        elif i == 'Y':
            color_wordle+="🟡"
    print(guesses_to_str([(guess,color_wordle)]))
    potential_words = []
    for word in words:
        if green_test(word, green_l(guess,feedback)) and yellow_test(word, yellow_l(guess,feedback)) and gray_test(word, gray_l(guess,feedback)):
            potential_words.append(word)
    
    return potential_words

def display_feedback (pw) -> None:
    print(f"Here are {len(pw)} words remaining.")
    print(gridify(pw))
    print('-'*80)


if __name__ == "__main__":
    # print(green_)test("smatk",green_l("slate","RRGGR")))
    # print(yellow_test("plaxe",yellow_l("slate","RRYYR")))
    # print(gray_test("zzezz",gray_l("slate","RRGRR")))
    # print(gray_l('slate','RRGRR'))

    # pass
    while True:
        guess, feedback = your_guess()
        if feedback == "GGGGG":
            break
            
        p_words = find_potential_words(p_words, guess, feedback)
        display_feedback(p_words)

    

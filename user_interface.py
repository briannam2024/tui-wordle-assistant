# Informatics INFO-I 210 - Summer 2023

"""
Wordle Assistant User Interface Elements
"""
from typing import Any, Hashable, Iterable, Optional
from data_handling import load_text



def count(data: Iterable) -> dict[Hashable, int]:
    coun = {}
    keys={}

    for i in range(len(data)):
        
        keys = data[i]
        
        num = data.count(data[i])
        coun[keys] = num

    return coun

def count_letters(words: list[str]) -> dict[str, int]:
    coun={}
    letters=""
    for i in words:
        letters += i
        for str in words:
            coun=count(letters)
    return coun


def guesses_to_str(guesses: list[tuple[str, str]]) -> str:
        line=""
        for str in guesses:
            for letter in str:
                line += letter + '\n'
        return line


def gridify(words: list[str]) -> str:
    grid = ""
    for i, word in enumerate(words):
        grid += f"  {word}"
        if (i + 1) % 10 == 0 and i != len(words) - 1:
            grid += "\n"
        elif (i + 1) % 50 == 0:
            grid += "\n"
            break
    return grid[:354]
# line 49: used outside source to understand enumerate
# https://www.youtube.com/watch?v=dNOeTt50e1M
# Data Science Tutorials, director. How to Loop with Indexes in Python | Loop through List with Both Content and Index | Python Basics. YouTube, YouTube, 4 Dec. 2019, https://www.youtube.com/watch?v=dNOeTt50e1M. Accessed 10 June 2023. 


def make_bar_tail(n: int) -> str:
    if n == 0:
        return ''
    if n == 1 or n == 2 or n == 3:
        return '░'
    if n == 4 or n == 5 or n == 6:
        return '▒'
    if n == 7 or n == 8 or n == 9:
        return '▓'



def make_bar(n: float) -> str:
    bar=""
    bar += '█'*int( n * 50)
    if (int(n*500)%10) > 1:
        bar += make_bar_tail(int(n*500)%10)
    else:
        return bar
    return bar




def counts_to_hist(counts: dict[Any, int], keys: Optional[list[Any]] = None) -> str:
    y_axis = ""
    dash = " |----|----|----|----|----|----|----|----|----|----|" + "\n" + " 0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0"
    
    if keys != None:
        for word in keys:
            num = float((counts[word])/100)
            y_axis += word + " " + make_bar(num) + "\n"
    else:
        for word in counts:
            num = float((counts[word])/100)
            y_axis += word + " " + make_bar(num) + "\n"

    return y_axis + dash + "\n"


if __name__ == "__main__":
    print(count_letters(["aaaaa", "aabba", "babab"]))

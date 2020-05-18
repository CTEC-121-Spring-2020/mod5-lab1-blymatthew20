"""
CTEC 121
Matthew Bly
Module 5 Lab 1
Moudle 5 Lab 1 code
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main1():
    print()
    print("Happy birthday to you!" )
    print("Happy birthday to you!" )
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")
    print()

# remove obvious duplication 
""" IPO happy()
Input(s): none
Process: prints/outputs chorus of happy birthday song
Output: prints tp terminal screen 
"""
def happy():
    print("Happy birthday to you!" )

def main2():
    print()
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()
    print()

# generalize for any person
""" IPO happyBDay()
Input(s): a name
Process: prints/outputs chorus of happy birthday song
Output: prints tp terminal screen 
"""
def happyBDay(name):
    print("Happy birthday, dear ", name, "...", sep="")

def main3():
    print()
    happy()
    happy()
    happyBDay('Yoshi')
    happy()
    print()
    
#combine song into a function
""" IPO singhappyBDay()
Input(s): a name
Process: prints/outputs happy birthday song
Output: prints tp terminal screen 
"""
def singHappyBDay(name):
    happy()
    happy()
    happyBDay(name)
    happy()
    print()

def main4():
    print()
    singHappyBDay('fred')
    singHappyBDay('lucy')
    singHappyBDay('bill')

main4()    
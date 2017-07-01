"""
examples of functions 
"""

def hows_the_parrot():
    print("he's flying around")
    
hows_the_parrot()

def lumberjack(name, pronoun):
        print("{} is the coolest and {} is smart".format(name, pronoun))
        print("{} sleeps all night and {} works all day.".format(name, pronoun))
        
        
def average(num1, num2):
    return (num1 + num2) / 2

avg = average(2, 8)
print(avg)

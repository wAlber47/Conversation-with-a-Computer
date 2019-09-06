"""
Simple program that creates a conversation between the user and the computer
Willie Alber 9/5/2019
"""
import time


# Gets the users name from input
def get_name():
    l_name = input("Hello! What is your name? ")  # stores the name of user in l_name (local name)
    l_name.capitalize()  # will capitalize the first letter on name

    s = l_name.split()  # checks for multiple words
    if len(s) > 1:
        print("Sorry, I don't quite understand what you mean.")  # asks the user to repeat just their name
        l_name = input("Can you please repeat just your name? ")
        l_name = l_name.capitalize()
        print("My bad " + l_name + ". Nice to meet you!")  # outputs the name
    else:
        l_name = l_name.capitalize()
        print("Nice to meet you " + l_name + ".")
    return l_name  # places the local name value inside of variable when function is called


# Gets the users age from input
def get_age():
    l_age = input("How old are you? ")
    return l_age


# Gets the users favorite color from input
def fav_color():
    i = input("Do you have a favorite color? [y/n] ")
    if i.lower == "yes" or i.lower() == "y":
        # hit if input is yet
        l_color = input("What is it? ")
        if l_color.lower() == "blue":
            print("Wow! Blue is my favorite color too!")
        elif l_color.lower() == "purple":
            print("I like purple too, but it's not my favorite.")
        else:
            print(l_color.capitalize() + " is such a cool color.")
    else:
        # hit if input is not yes
        print("That's okay, I guess not everybody likes colors as much as me. ")
        l_color = input("If you had to pick, which one would it be? ")
    return l_color


# Gets the users favorite programming language from input
def fav_language():
    l_lang = input("What is your favorite programming language? ")
    print("My favorite is binary, but you already knew that!")
    return l_lang


def recap(name, color, age, language):
    print("I had such a great conversation with you " + name + ".")
    time.sleep(2)
    print("Let me quickly recap everything I just found out about you!")
    time.sleep(2)
    print("You're favorite color is " + color + ".")
    time.sleep(2)
    print("Currently, you are likely " + str(age) + " years old.")
    time.sleep(2)
    print("Your favorite programming language is " + language + ". That's a good one.")
    time.sleep(2)
    print("I hope you come chat with me again soon! Bye!")


name = get_name()  # runs get_name function and store the result in name
age = get_age()  # runs get_name and gets year of birth from that
year = 2019 - int(age)
print("So if you're " + age + ", that means you were most likely born in", str(year) + ".")
altair = 44  # first computer was bult in 1975, and is 44 years old
# compares ages and gets a difference is ages
if altair > int(age):
    diff = altair - int(age)
    print("I am " + str(diff) + " years older than you " + name + ".")
elif altair < int(age):
    diff = int(age) - altair
    print(name + ", you are " + str(diff) + " years older than me.")
else:
    print("We are the same age!")
color = fav_color() # calls fav_color and stores result in color
time.sleep(2)
language = fav_language()  # calls fav_language and stores result in language
time.sleep(2)

recap(name, color, age, language)





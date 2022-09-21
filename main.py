from tkinter import E


def vowel_consonant():
    vowel = ["a", "e", "i", "o", "u"]

    char = input("please enter a letter from the alphabet (a-z or A-Z): ").lower()

    if char in vowel:
        print(f"the letter {char} is a vowel")
    else:
        print(f"the letter {char} is a consonant")

# vowel_consonant()

def phrase_length():
    running = True
    while running:
        string = input("please enter a word or a phrase: ")
        if string == "quit":
            running = False
        else:
            strlength = len(string)
            print(f"What you entered is {strlength} characters long")

# phrase_length()

def dog_years():
    human_years = int(input("Input a dog's age in human years: "))
    dog_years = 0
    for years in range(human_years):
        if years < 2:
            dog_years += 10 
        else:
            dog_years += 7

    return (f"The dog's age in dog years is {dog_years}")

# print(dog_years())

def triangle_type():
    print("Enter the lengths of a three sided triangle:")
    a = input(" a: ")
    b = input(" b: ")
    c = input(" c: ")
    if (a == b and b == c):
         type ="equalateral"
    elif ( a == b or b == c or a == c):
         type = "isoceles"
    else:
         type = "scalene"
    return(f"a triangle with sides of {a}, {b} & {c}, is a {type} triangle")

# print(triangle_type())

def fibonacci_sequence():
    length = int(input("How long do you want the fibonnaci sequence to be? "))
    array = [x for x in range(length)]
    print(array)
    for n in range(len(array)):
        if n < 2: 
            number = n
            print(f"term: {n} / number: {number}")
        else:
            number = array[n -1] + array[n -2]
            print(f"term: {n} / number: {number}")
        
# fibonacci_sequence()

def season_finder():
    user_month = input("Enter the month of the year (Jan - Dec): ")
    user_day = input("Enter the day of the month: ")

    if user_month in ('Jan', 'Feb', 'Mar'):
        season = 'winter'
    elif user_month in ('Apr', 'May', 'Jun'):
        season = 'spring'
    elif user_month in ('Jul', 'Aug', 'Sep'):
        season = 'summer'
    else:
        season = 'autumn'
    
    if (user_month == 'March') and (user_day > 19):
        season = 'spring'
    elif (user_month == 'Jun') and (user_day > 20):
        season = 'summer'
    elif (user_month == 'September') and (user_day > 21):
        season = 'autumn'
    elif (user_month == 'December') and (user_day > 20):
        season = 'winter'
    
    print(f"{user_month} {user_day} is in {season}")

season_finder()
    

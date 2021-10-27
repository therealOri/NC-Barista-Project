#START

# Imports for fancy and smooth terminal stuffs.
import time
import sys
import os

# Defining clear(). So I don't have to type "os.system('clear||cls')" so much. It also looks better.
def clear():
    os.system('clear||cls')


clear()
print("Hello! Thank you for comming in today!")
name = input("What is your name?: ")
clear()

# Prices for the menu items.
price1 = 1.00
price2 = 3.00
price3 = 2.75
price4 = 3.50

# Where we add onto our menu! I could do some other python3 tricks with lists and dictionaries but this feels/seems more simple.
menu = f"""
1: Black Coffe | ${price1}
2: Carmel Mocha | ${price2}
3: Espresso | ${price3}
4: Latte Mocha | ${price4}
"""

# Add more options here if we want to expand our menu to include foods or more drinks.
drink1 = "Black Coffe"
drink2 = "Carmel Mocha"
drink3 = "Espresso"
drink4 = "Latte Mocha"

print(f"Welcome {name}! Please choose from our menu below what you would like!")
print(menu)


# Making sure it keeps looping if you enter any number higher than 4/how many items we have on our menu. Or if #the number is 0. 
# If numbers 1-4 gets entered, then it'll break the loop and continue.
while True:
    option = input("Option: ")
    ammount = input("How many?: ")


    try:
        option = int(option)
        ammount = int(ammount)
    except Exception as e:
        print(f"Oops! The value(s) you gave me was not and number/Integer.\nError: {e}")
        quit()

    if option > 4:
        clear()
        print(f"Sorry, We don't have an item for that number/option. Please pick again!\n{menu}")
    if option == 0:
        clear()
        print(f"Sorry, We don't have an item for that number/option. Please pick again!\n{menu}")
    elif ammount == 0:
        clear()
        print(f'Sorry, but you need to order something from the menu. Please pick again!\n{menu}')
    
    # I am sure there is a much better way of doing this but ehh..It works.
    elif option == 1:
        clear()
        print(f"Thank you for ordering {ammount} {drink1}(s). Your order will be done shortly!")
        break
    elif option == 2:
        clear()
        print(f"Thank you for ordering {ammount} {drink2}(s). Your order will be done shortly!")
        break
    elif option == 3:
        clear()
        print(f"Thank you for ordering {ammount} {drink3}(s). Your order will be done shortly!")
        break
    elif option == 4:
        clear()
        print(f"Thank you for ordering {ammount} {drink4}(s). Your order will be done shortly!")
        break



# Counts down from 15. I did not make this counter. I found it here: https://stackoverflow.com/a/5853003/15114290. So...credits to them!
for remaining in range(15, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("[{:2d}] seconds remaining.".format(remaining)) 
    sys.stdout.flush()
    time.sleep(1)

clear()
# I am also sure this could have been done better or differently..but once again, ehh..it works.
# We would also add onto this if there are more options added to the menu and all that.
if option == 1:
    total1 = round(ammount * price1)
    print(f"\r{name}! Your {ammount} {drink1}(s) is ready! *places your order on the counter*. And your total is: ${total1}\nPlease come and pick up your order! <3")
if option == 2:
    total2 = round(ammount * price2)
    print(f"\r{name}! Your {ammount} {drink2}(s) is ready! *places your order on the counter*. And your total is: ${total2}\nPlease come and pick up your order! <3")     
if option == 3:
    total3 = round(ammount * price3)
    print(f"\r{name}! Your {ammount} {drink3}(s) is ready! *places your order on the counter*. And your total is: ${total3}\nPlease come and pick up your order! <3")     
if option == 4:
    total4 = round(ammount * price4)
    print(f"\r{name}! Your {ammount} {drink4}(s) is ready! *places your order on the counter*. And your total is: ${total4}\nPlease come and pick up your order! <3")

#END

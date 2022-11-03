"""
Purpose: offer the user a choice of food items, calculate total bill
Pre-conditions: user enters 5 or 6 y's or n's depending on desired items(strings)
Post-conditions: prompts for choices, total bill before(float) and after tip, (float)
"""
print("Welcome to Dairy King")
print("Please answer each question with y or n")
total = 0
 
dict = {"Grilled cheese":7.00, "Nachos":5.00, "Chicken":8.00, "Hamburger":8.00, "Cheeseburger":10.00, "Hot Dog":6.00}
for i in dict:
    print(i, dict[i])

if input("Do you want a grilled cheese sandwich? ") == "y":
    total += 7
if input("Do you want a serving of nachos? ") == "y":
    total += 5 
if input("Do you want a chicken sandwich? ") == "y":
    total += 8

while input("Do you want a Hamburger? ") == "y":
    total += 8
    if input("Do you want cheese on that? ") == "y":
        total += 2
        break
if input("Do you want a hot dog? ") == "y":
    total += 6

print(f"The total for your food is ${total:.2f}\nThe total with 20% tip is ${(total * .2) + total:.2f}\nThank you for your business!")

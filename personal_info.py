
# Personal Information Manager
# Created by: Nagi Reddy
# Description: Stores and displays personal information
# Static information
# Static information
name = "Nagi Reddy"
age = 20
city = " KADAPA "
hobby = "Cricket"
print("Welcome to Personal Info Manager!")

favorite_food = input("Enter your favorite food: ")

while favorite_food == "":
    print("Food cannot be empty!")
    favorite_food = input("Enter your favorite food: ")

favorite_color = input("Enter your favorite color: ")

while favorite_color == "":
    print("Color cannot be empty!")
    favorite_color = input("Enter your favorite color: ")
age_in_months = age * 12
print("\n" + "=" * 40)
print("PERSONAL INFORMATION")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age} ({age_in_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")

print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

print("Thank you for using the program!")
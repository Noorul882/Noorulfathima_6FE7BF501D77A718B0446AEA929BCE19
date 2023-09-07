#Write a program that determines whether a year entered by the user is a leap year 
# Get the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
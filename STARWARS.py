#Marisa Gross
#starwars.py
#Week 3: Star Wars Name 

#This program tells you your Starwars name.


def main():
    print("This program illustrates your Starwars name")
    lastName=input("Please enter your last name: ")
    firstName=input("Please enter your first name: ")
    maidenName=input("Please enter your mother's maiden name: ")
    townName=input("Please enter the town in which you were born: ")  
    
    print(lastName[0:3] + firstName[0:2], maidenName[0:2] + townName[0:3])

main()

#Prompt the user to input their First and Last name and their mother's maiden name and the city where they where born.
# Calculate their "Star Wars" name.  
# Print out their "Star Wars" name.
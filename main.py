import csv
import project
import math


# Function 0
# We have coded a function below that converts a string to uppercase or lowercase
def convertCase(original_string, case): 
    if case == "Upper":
        converted_string = original_string.upper()
    elif case == "Lower":
        converted_string = original_string.lower()
    else:
        print("Unknown case, keeping string unchanged")
        converted_string = original_string
    return converted_string


# Function 1
# Write the reverseString(original_string) function here
# This function should return the reversed version of original_string
# For example, if original_string was equal to "mary", the function should return "yram"
# Note: You shouldn't use print in this function.




# Function 2
# Write the checkPalindrome(original_string) function here.
# This function should return True if original_string is a palindrome, otherwise False.
# Note: You shouldn't use print in this function.
# Hint: Use the function you have defined above!



# Function 3
# Write the findPalindromeMovieName() function here
# This function should return the title of the movie in the dataset which is a palindrome. 
# Note: There is only one such movie in the dataset!
# Note: You shouldn't use print in this function.
# Hint: Use the function you have defined above!




# Function 4
# Write the encodeString(original_string) function here
# Replace all 'A' and a' with '@', all 'O' and 'o' with '0' and all 'I' and 'i' with '!'
# This function should return the original_string, after encoding it
# Note: You shouldn't use print in this function.



# Function 5
# Write the countMoviesByDirector(director_name) function here
# Count the number of movies by the given director
# This function should return an integer, the number of movies released by director_name
# Note: You shouldn't use print in this function.
# Hint: For each movie in the dataset, check who was the director



# Function 6
# Write the findSecondHighestRevenue(year) function here
# This function should return the revenue of the second largest grossing movie in the given year
# Note: You shouldn't use print in this function
# Hint: For each movie in the dataset, check when it was released and its revenue
# Hint: To find the second highest revenue, you may need to also keep track of the highest revenue!




# Function 7
# Write the findKeyword(plot_keyword, movie) function here
# Step1: Retrieve movie description for the given movie
# Step2: Use string find function check if the movie description has the desired plot keyword
# Step3: If the keyword is present then return "Yes", otherwise "No"
# Note: You shouldn't use print in this function.




# Function 8
# Write the mainActor(movie) function here
# Step1: Get the movie's cast by using our getMovieData function.
# Step2: Retrieve the main actor's name by slicing the string. The main actor is listed first.
# Step2: Return the string containing the main actor's name
# Note: You shouldn't use print in this function.




def main():

    # In each of the below problems, edit only the print(0) statement.

    # Read and understand Function 0 which we have written for you above. 
    # Use it in Problems 1 and 2
    print("Problem 1")
    print("The lowercase version of the string \"The Last Samurai\" is : ")
    print(0)
    print()

    print("Problem 2")
    print("The uppercase version of the string \"Fight Club\" is : ")
    print(0)
    print()

    # Practice reading data from the dataset 
    # (read and understand the instructions in the readme file carefully)
    print("Problem 3")
    print("The director of \"La La Land\" is : ")
    print(0)
    print()

    print("Problem 4")
    print("\"Sherlock Holmes\" was released in : ")
    print(0)
    print()

    print("Problem 5")
    print("The cast of the movie ranked 320th in the dataset: ")
    print(0)
    print()

    # Make sure you complete writing Function 1
    print("Problem 6")
    print("Lets reverse the string \"madagascar\". The reversed string is : ")
    print(0)
    print()

    # Make sure you complete writing Function 2
    print("Problem 7")
    print("The string \"Spacecaps\" is a Palindrome ")
    print(0)
    print()

    # Make sure you complete writing Function 3
    print("Problem 8")
    print("A movie whose name is a palindrome in the given dataset is : ")
    print(0)
    print()

    # Make sure you complete writing Function 4
    print("Problem 9")
    print("Using the encodeString(original_string) we can convert the string \"Password\" to the string: ")
    print(0)
    print()

    # Make sure you complete writing Function 5
    print("Problem 10")
    print("The total number of movies in the dataset that are directed by Christopher Nolan are: ")
    print(0)
    print()

    # Make sure you complete writing Function 6
    print("Problem 11")
    print("The second-highest grossing movie of 2016 had a revenue of: ")
    print(0)
    print()

    # Make sure you complete writing Function 7
    print("Problem 12")
    print("Is \"The Prestige\" a \"Mystery\" movie? ")
    print(0)
    print()

    print("Problem 13")
    print("Is \"Kimi no na wa\" a \"Fantasy\" movie? ")
    print(0)
    print()

    # Make sure you complete writing Function 8
    print("Problem 14")
    print("The main actor in \"Black Swan\" is: ")
    print(0)
    print()

    print("Problem 15")
    print("The main actor in \"Inception\" is: ")
    print(0)
    print()



if __name__ == "__main__":
    main()
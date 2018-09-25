import csv
import project
import math

# Function 0
# We have coded a function below that prints out the camelCase version of the string input
# Why do we have this? The students wont understand what is going on in the code, need knowledge of lists
def printCamelCase(string): #better if variable name is not string, may be confusing to students
    split = string.lower().split()
    first = split[0].lower()
    result = [first]
    for word in split[1:]:
        result.append(word.capitalize())
    return ''.join(result)

# Function
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
def reverseString(original_string):
    reversed_string = ""
    for i in range(len(original_string)):
        reversed_string = original_string[i] + reversed_string
    return reversed_string


# Function 2
# Write the checkPalindrome(original_string) function here.
# This function should return True if original_string is a palindrome, otherwise False.
# Note: You shouldn't use print in this function.
# Hint: Use the function you have defined above!
def checkPalindrome(original_string):
    reversed_string = reverseString(original_string)
    return original_string.lower()==reversed_string.lower()


# Function 3
# Write the findPalindromeMovieName() function here
# This function should return the title of the movie in the dataset which is a palindrome. 
# Note: There is only one such movie in the dataset!
# Note: You shouldn't use print in this function.
# Hint: Use the function you have defined above!
def findPalindromeMovieName():
    for i in range(1,1001):
        movie_title = project.getMovieData('Title',Rank=i)
        if checkPalindrome(movie_title):
            return movie_title

# Function 4
# Write the encodeString(original_string) function here
# Replace all 'A' and a' with '@', all 'O' and 'o' with '0' and all 'I' and 'i' with '!'
# This function should return the original_string, after encoding it
# Note: You shouldn't use print in this function.
def encodeString(original_string):
    encoded_string = ""
    for i in range(len(original_string)):
        c = original_string[i]
        if c=='A' or c=='a':
            encoded_string = encoded_string + '@'
        elif c=='O' or c=='o':
            encoded_string = encoded_string + '0'
        elif c=='I' or c=='i':
            encoded_string = encoded_string + '!'
        else:
            encoded_string = encoded_string + c
    return encoded_string


# Function 5
# Write the countMoviesByDirector(director_name, year) function here
# Count the number of movies by the given director in the given year
# This function should return an integer, the number of movies released by director_name in year
# Note: You shouldn't use print in this function.
# Hint: For each movie in the dataset, check when it was released and who was the director
def countMoviesByDirector(director_name):
    count = 0
    for i in range(1,1001):
        movie_dir = project.getMovieData('Director',Rank=i)
        if movie_dir==director_name:
            count = count + 1
    return count

# Function 6
# Write the findSecondHighestRevenue(year) function here
# This function should return the revenue of the second largest grossing movie in the given year
# Note: You shouldn't use print in this function
# Hint: For each movie in the dataset, check when it was released and its revenue
# Hint: To find the second highest revenue, you may need to also keep track of the highest revenue!
def findSecondHighestRevenue(year):
    highest = 0
    second_highest = 0
    for i in range(1,1001):
        movie_year = project.getMovieData('Year',Rank=i)
        movie_rev = project.getMovieData('Revenue',Rank=i)
        if movie_year==year:
            if movie_rev>highest:
                second_highest = highest
                highest = movie_rev
            elif movie_rev>second_highest:
                second_highest = movie_rev
            else:
                continue
        else:
            continue
    return second_highest


# Function 7
# Write the findKeyword(movie_description) function here
# Step1: Loop through all the rows of the dataset by index
# Step2: Retrieve movie description using our getMovieData(field, MovieName=None, Rank=None) function
# Step2: Use string find function check if the movie description has the desired plot keyword
# Step3: If the keyword is present break out of your loop and return the movie name
# Note: You shouldn't use print in this function.
def findKeyword(keyword):
    for i in range(1,1001):
        movie = project.getMovieData("Title",Rank=i)
        description = project.getMovieData("Description",Rank=i)
        if description.lower().find(keyword.lower())!=-1:
            return movie
    return False

# Funstion 8
# Write the mainActor(movie) function here
# Step1: Get the movie's cast by using our getMovieData function.
# Step2: Retrieve the main actor's name by slicing the string. The main actor is listed first.
# Step2: Return the string containing the main actor's name
# Note: You shouldn't use print in this function.

def mainActor(movie):
    cast = project.getMovieData("Actors", MovieName=movie)
    index = cast.find(',')
    main_actor = cast[0:index]
    return main_actor

def main():

    print("Problem 0")
    print(" The camel case version of the string \"The Last Samurai\" is : ")
    print(0)
    print()

    print("Problem 1")
    print("Lets reverse the string \"Madagascar\" . The reversed string is : ")
    print(0)
    print()

    print("Problem 2")
    print("Is the string \"spacecaps\" a Palindrome : ")
    print(0)
    print()

    print("Problem 3")
    print("A movie whose name is a palindrome in the given dataset is : ")
    print(0)
    print()

    print("Problem 4")
    print("Using the encodeString(original_string) we can convert the string \"Password\" to the string: ")
    print(0)
    print()

    print("Problem 5")
    print("Using the encodeString(original_string) we can convert the string \"Password\" to the string: ")
    print(0)
    print()

    print("Problem 6")
    print("The total number of movies in the dataset that are directed by James Gunn are: ")
    print(0)
    print()




if __name__ == "__main__":
    main()
    #print(reverseString("Hello"))
    #isPalidrome()
    #project.describe_data()
    print(mainActor("Gold"))
    print(countMoviesByDirector("James Gunn"))
    #print(printCamelCase("You have got Mail"))
    print(project.getMovieData("Description", MovieName="Gold", Rank=None))
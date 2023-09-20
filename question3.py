"""

    ASSIGNMENT #1
    QUESTION 3
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""

print("Please inform the string: ")
myString = input()

stringLength = len(myString)

print("\n------------------------------")
print("Informed string is: " + myString)
print("The length of the string is: " + str(stringLength))
print("------------------------------")

if stringLength <= 7:
    print("\nThe string length is smaller or equal to 7.")
else:
    if (stringLength % 2) == 0:
        
        print("\nThe string length is not odd.")
        
    elif (stringLength % 2) != 0:
            
        letter = [char for char in myString]

        middleIndex = stringLength // 2

        print("\n------------------------------")
        print(letter[middleIndex-1] + letter[middleIndex] + letter[middleIndex+1])
        print("------------------------------")



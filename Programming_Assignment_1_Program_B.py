#Joey Rudolph
#9/13/2021
#This program takes in the heights of each of the users and calculates the average heights of the group
def height_Calculator():
    number_of_people = int(input("How many people are in your group : ")) #Takes in the number of people from the group of the user
    total_height_in_inches = 0 #Initiates accumulator variable
    total_height_in_meters = 0 #Initiates accumulator variable
    

    
    for i in range(number_of_people): #Loops through number of people
        print()
        print("Person ", i+1)
        height_in_feet, inches = eval(input("Enter your height in feet and inches separated by a comma : ")) #Takes in the height in feet and inches of the user
        height_in_inches = (height_in_feet * 12) + inches #Converts input to inches
        height_in_meters = (height_in_inches * 2.54)/(100) #Converts input to meters
        print("Height of person ", i+1, " in feet and inches : ", height_in_feet,"'" , inches,'"', sep="") #Returns output to the user
        print("Height of person ", i+1, " in meters : ", height_in_meters) #Returns output to the user
        total_height_in_inches += height_in_inches #Accumulate total inches
        total_height_in_meters += height_in_meters #Accumulate total meters
        print()
        
    average_height_in_meters = total_height_in_meters/number_of_people #Finds the average in meters
    average_height_in_inches = total_height_in_inches/number_of_people #Finds the average in inches
    average_feet = average_height_in_inches // 12 # // division sign to get a whole number for feet
    final_inches = average_height_in_inches % 12 # % Gets the remainder of inches
    print("The average height of the group in meters is : ",  average_height_in_meters) #Returns output to the user
    print("The average height of the group in feet and inches is : ", int (average_feet), "' ", final_inches, '"', sep = "") #Returns output to the user
    
    
height_Calculator() #Calls the function

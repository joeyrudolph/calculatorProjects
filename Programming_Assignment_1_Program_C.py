#Joey Rudolph
#Due date : 9/20/2021
#Programming Assignment 1 Program C
#This program tells the ith fibonacci number based on user input. 
def fibonacci_Numbers():
    fn_1 = 0 #Declaring first fibonacci number
    fn_2 = 1 #Declaring second fibonacci number
    fibonacci = [0,1] #Creates list to keep track of the fibonacci numbers
    print("The first 2 fibonacci numbers are 0 and 1")
    number = eval(input("Enter a positive integer greater than 2 : ")) #User input
    

    print("The first", number, "fibonacci numbers are",end = " ")
    
    for i in range(2,number):# i goes up to user input (number)
        total_sum = fn_1 + fn_2 # Adding first and second fibonacci number to total_sum variable
        fn_1 = fn_2 #Redefining sum_1 as sum_2
        fn_2 = total_sum #Redefining sum_2 as total_sum
        fibonacci.append(fn_2) #Adds sum_2 to the fibonacci sequence
    print(fibonacci)    
    print()
    print("Fibonacci number", number, "is", fn_2)
        
fibonacci_Numbers() #Calls the function

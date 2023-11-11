#Joey Rudolph
#9/13/2021
#This program takes in soccer stats inputs and returns the averages for each game and for the season
def soccerCalculator():
    print("If you play soccer, please answer the following questions")
    total_number_of_games_played_during_the_season = int(input("How many games did you play this season : ")) #Asks the user how many games he/she played this season

    
    if total_number_of_games_played_during_the_season < 1: #Checks to make sure user enters a number 1 or greater in order to run program
        print("Please enter a number 1 or greater for how many games you played this season")
        soccerCalculator() #Calls function again if this condition is met

        
    total_goals_scored_during_the_season = 0 #Initiates accumulator variable
    total_shots_on_goal_during_the_season = 0 #Initiates accumulator variable
    shots_on_goal = 0 #Initiates shots_on_goal (number of shots on goal for each game)
    goals_scored = 0 #Initiates goals_scored (number of goals for each game)
    print() #Creates empty line
    print() #Creates empty line

    
    for i in range(total_number_of_games_played_during_the_season): #Loops through total_number_of_games_played_during_the_season
        print("Game ", i+1) #Labels the ith game
        shots_on_goal = eval(input("How many shots on goals did you have this game? : ")) #Takes in shots on goal as an input
        goals_scored = eval(input("How many goals did you score this game? : ")) #Takes in goals scored as an input
        
        if goals_scored == 0 & shots_on_goal >= 1: #Condition 1 (for the statistics of each individual game)
           print("You scored 0 percent of your shots on goal this game")
           print() #Creates empty line
           print() #Creates empty line

        elif goals_scored == 0 & shots_on_goal == 0: #Condition 2 (for the statistics of each individual game)
            print("You scored 0 percent of your shots this game")
            print() #Creates empty line
            print() #Creates empty line
        
        elif goals_scored > shots_on_goal: #Condition 3 (statistically incorrect input for the statistics each individual game)
            print("The numbers you have entered are statistically incorrect")
            print() #Creates empty line
            print("Please re enter your inputs")
            print() #Creates empty line
            soccerCalculator() #Calls the functions again only if condition 3 is satisfied
            print() #Creates empty line
            print() #Creates empty line

        else: #Condition 4 (for the statistics of each individual game)
            percent_of_shots_scored = (goals_scored)/(shots_on_goal)
            percent_of_shots_scored *= 100 #Multiplies percentage variable by 100
            total_goals_scored_during_the_season += goals_scored #Accumulate total_goals_scored
            total_shots_on_goal_during_the_season += shots_on_goal #Accumulate total_shots_on_goal
            print("You scored on ", percent_of_shots_scored, " percent of your shots on goal this game")
            print() #Creates empty line
            print() #Creates empty line

    
    if total_goals_scored_during_the_season == 0 & shots_on_goal >= 1: #Condition 1 (for the statistics of the whole season)
        print("You have scored 0 percent of your shots on goal this season")
        print() #Creates empty line
        print() #Creates empty line

    elif total_goals_scored_during_the_season == 0 & shots_on_goal == 0: #Condition 2 (for the statistics of the whole season)
        print("You have scored 0 percent of your shots on goal this season")
        

    else: #Condition 3 (for the statistics of the whole season)
        average_number_of_goals_scored_per_game = total_goals_scored_during_the_season/total_number_of_games_played_during_the_season #Finds the average in goals scored per game
        average_percentage_of_shots_that_led_to_goals = total_goals_scored_during_the_season/total_shots_on_goal_during_the_season #Finds the average percent in shots that led to goals
        print()
        print()
        print("You averaged ", average_number_of_goals_scored_per_game, " goals per game this season") #Returns output to the user
        average_percentage_of_shots_that_led_to_goals *= 100 #Multiplies percentage variable by 100
        print("You scored on ", average_percentage_of_shots_that_led_to_goals, " percent of your shots on goal this season") #Returns output to the user
        print() #Creates empty line
        print() #Creates empty line
        
soccerCalculator() #Calls the function

#TA Tyler Sibley helped me come up with this idea. He asked me what my interests were and soccer immediately came to mind. That is why I decided to make a soccer related program.



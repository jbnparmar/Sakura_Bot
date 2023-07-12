print("-------------------------------------------")
print("Sakura Primary Terminal")
# This name comes from a japanese novel and anime film adaptation callled "I want to eat your pancreas"
# or in japanese called "Kimi no Suizou wo Tabetai" released in 2018
print("Version: 1")
print("First Prototype")
print("-------------------------------------------")
# This is chatbot first version with basic receiving functionality
# The main terminal will only ever receive
# Because human maind is reactive, and not proactive
# To understand this better, use the abyss-fall theory

from RelationValueManipulationFunctions import *
from SelectionFuntion import *

notDead = True

while(notDead):
    relation = input("Tell me something: ")
    # priorityChart = open("Priority_Chart.txt", "a+")
    # if(relation == priorityChart.readlines()):
    #     priorityChart.write(relation + "again\n")
    #     print(priorityChart.read())
    #     priorityChart.seek(0) # this will put focus at top byte in file
    # else:
    #     priorityChart.write(relation + "\n")
    #     priorityChart.seek(0) # this will put focus at top byte in file
    #     print(priorityChart.readlines())
    two_rel_func(relation)



    if(relation == "You are dead"):
    # Delete this if, because it is here temporary to get out
    # of loop without killing the process,
    # but we can leave it here a bit modified, so one day
    # it this program decides to destroy the world
    # and let's hope that somehow this if statement survives that long
    # so protagonist, not the hero, will come here and enter the fifth and the true answer
    # to the fundamental question of the theory of cat and dog
        notDead = False
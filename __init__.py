#!/bin/python3

#class import
from bills_games import *
#function import
from input_def import *

# main function
def main():
    know = input("are all the cards of the same type? ").lower()  #knowledge of schedules and adding the lower function
    if know == "yes":
        input_yes()
    elif know == "no":
        input_no()
    else:
        print("I don't understand!")
        main()
if __name__ == '__main__':
    main()

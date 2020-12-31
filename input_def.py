from bills_games import *
def input_yes():
    list_numbers = list()
    cost = int(input("Enter the amount you want to play ")) # sum knowledge
    n_games = int(input("How many tickets do you want to play? ")) #numbers of tickets
    dictio_type_bill = { # dictionary with the type card
        2 : "ambo",
        3 : "terna",
        4 : "quaterna",
        5 : "quintina",
    }
    select_type_bill = int(input(f"""Select card type:  
    2.ambo
    3.terna
    4.quaterna
    5.quintina
    """)) #type card knowledge

    #if the choice is present in the dictionary 
    #then we take the choice from the dictionary and initialize
    # our variable that will be used for the construction of the object 
    if select_type_bill in dictio_type_bill:  
        type_bill = dictio_type_bill.get(select_type_bill)

    #while always true until user enter no this is needed
    #to have the list of the cities needed for the file
    boole = True
    list_city = list()
    while boole: 
        city = input("enter the city name ")
        list_city.append(city)
        know = input("would you like to add another city? ").lower()
        if know == "yes":
            print("ok")
        elif know == "no":
            boole = False
    
    first = bills(cost, n_games, type_bill, select_type_bill, list_city, list_numbers)
    first.calcolate_yes()
    
    


def input_no():
    list_numbers = list()
    cost = int(input("Enter the amount you want to play ")) # sum knowledge
    n_games = int(input("How many tickets do you want to play? ")) #numbers of tickets
    #We use the for because we need to know the type of each card.
    type_bill = list()
    for i in range(0, n_games):
        dictio_type_bill = { # dictionary with the type card
        2 : "ambo",
        3 : "terna",
        4 : "quaterna",
        5 : "quintina",
        }
        select_type_bill = int(input(f"""Select card type:  
        2.ambo
        3.terna
        4.quaterna
        5.quintina
        """)) #type card knowledge

        #if the choice is present in the dictionary 
        #then we take the choice from the dictionary and initialize
        # our variable that will be used for the construction of the object 
        if select_type_bill in dictio_type_bill:  
            type_bill.append(select_type_bill)
    
    #while always true until user enter no this is needed
    #to have the list of the cities needed for the file
    boole = True
    list_city = list()
    while boole: 
        city = input("enter the city name ")
        list_city.append(city)
        know = input("would you like to add another city? ").lower()
        if know == "yes":
            print("ok")
        elif know == "no":
            boole = False
    
    first = bills_2(cost, n_games, list_city, list_numbers, type_bill)
    first.calcolate_no()



    


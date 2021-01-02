from bills_games import *
def input_yes():
    try:
        list_numbers = list()
        cost = int(input("Enter the amount you want to play: ")) # sum knowledge
        n_games = int(input("How many tickets do you want to play? min=1, max=10: ")) #numbers of tickets
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
        numbers = int(input("how many numbers do you want to play, min=1, max=10: "))

        first = bills(cost, n_games, type_bill, select_type_bill, list_numbers, numbers)
        first.calcolate_yes()
    except ValueError:
        print("I don't understand!, Repeat")
        input_yes()


def input_no():
    try:
        list_numbers_1 = []
        list_numbers = list()
        cost = int(input("Enter the amount you want to play: ")) # sum knowledge
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
            """))#type card knowledge
            if select_type_bill in dictio_type_bill:  
                type_bill.append(dictio_type_bill.get(select_type_bill))
            numbers = int(input("How many numbers do you want to play, min=1, max=10: "))
            list_numbers_1.append(numbers)

            #if the choice is present in the dictionary 
            #then we take the choice from the dictionary and initialize
            # our variable that will be used for the construction of the object 

        #while always true until user enter no this is needed
        #to have the list of the cities needed for the file
        first = bills_2(cost, n_games, type_bill, list_numbers, list_numbers_1)
        first.calcolate_no()
    except ValueError:
        print("I don't uderstand, Repeat")
        input_no()



    


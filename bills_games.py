import random
class bills:
    def __init__(self, cost, n_games, type_bill, list_type_bill, list_numbers, numbers):
        self.cost = cost
        self.n_games = n_games
        self.type_bill = type_bill
        self.list_type_bill = list_type_bill
        self.list_numbers = list_numbers
        self.numbers = numbers

    def calcolate_yes(self):
        for c in range(1, self.n_games+1):
            print("************stampo la " + str(c) + " schedina******************")
            self.list_numbers.clear()
            for v in range(0, self.numbers):
                rand = random.randint(1 ,90)
                self.list_numbers.append(rand)
            print("these numbers " + str(self.list_numbers) + " Type: " + str(self.type_bill))



class bills_2(bills):
    def __init__(self, cost, n_games, type_bill,  list_numbers, numbers):
        self.cost  = cost
        self.n_games = n_games
        self.type_bill  = type_bill
        self.list_numbers  = list_numbers
        self.numbers = numbers

        


    def calcolate_no(self):
        index_numbers = 0
        index_type_bill = 0
        for games in range(1, self.n_games+1):
            self.list_numbers.clear()
            print("************stampo la " + str(games) + " schedina******************")
            try:
                for giro in range(0, self.numbers[index_numbers]):
                    rand = random.randint(1 ,90)
                    self.list_numbers.append(rand)
                print(" has these numbers " + str(self.list_numbers) + " Type :" + self.type_bill[index_type_bill])
                index_numbers += 1
                index_type_bill += 1
            except IndexError:
                print("ok ho finito")       
        
    

    
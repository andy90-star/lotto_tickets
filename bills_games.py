import random
class bills:
    def __init__(self, cost, n_games, type_bill, list_type_bill, list_city, list_numbers):
        self.cost = cost
        self.n_games = n_games
        self.type_bill = type_bill
        self.list_type_bill = list_type_bill
        self.list_city = list_city
        self.list_numbers = list_numbers

    def calcolate_yes(self):
        for c in range(1, self.n_games+1):
            print("************stampo la " + str(c) + " schedina******************")
            for i in self.list_city:
                self.list_numbers.clear()
                for v in range(0, self.list_type_bill):
                    rand = random.randint(1 ,90)
                    self.list_numbers.append(rand)
                print("the city " + str(i) + " has these numbers " + str(self.list_numbers))

    

class bills_2(bills):
    def __init__(self, cost, n_games, list_city, list_numbers, type_bill):
        self.cost  = cost
        self.n_games = n_games
        self.list_city  = list_city
        self.list_numbers  = list_numbers
        self.type_bill  = type_bill

        


    def calcolate_no(self):
        for c in range(1, self.n_games+1):
            print("************stampo la " + str(c) + " schedina******************")
            for i in self.list_city:
                for v in self.type_bill:
                    print(v)
                    self.list_numbers.clear()
                    for g in range(0, v):
                        rand = random.randint(1 ,90)
                        self.list_numbers.append(rand)
                print("the city " + str(i) + " has these numbers " + str(self.list_numbers))
    
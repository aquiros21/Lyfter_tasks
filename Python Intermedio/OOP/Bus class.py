class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers_on_board = []

    def take_passenger(self, person):
        if len(self.passengers_on_board) >= self.max_passengers:
            print("Bus is full!")
        else:
            self.passengers_on_board.append(person)
    
    def drop_passenger(self,person):
        if len(self.passengers_on_board) == 0:
            print("Bus is already empty!")
        else:
            self.passengers_on_board.remove(person)


bus1 = Bus(2)

bus1.take_passenger("Adrian")
bus1.take_passenger("Andres")
bus1.drop_passenger("Adrian")
bus1.drop_passenger("Andres")

print(bus1.passengers_on_board)
import time, random, math, datetime

abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Field:
    def __init__(self, shape = [10, 10], mines = 10, array = []):
        self.shape = shape
        self.mines = mines
        if array == []:
            self.array = [[1] * self.shape[0]] * self.shape[1]
            self.fill_mines()
        else:
            self.array = array
    
    def correct_format(self, position):
        correct = True
        if not position[0].isalpha():
            correct = False
        if not position[1].isdigit():
            correct = False

        if correct:
            return True
        else:
            return False
    
    def fill_mines(self):
        mine_positions = []
        for n in range(0, self.mines):
            mine = random.randint(0, self.shape[0] * self.shape[1])
            if not mine in mine_positions:
                mine_positions.append(mine)
            else:
                while True:
                    mine = random.randint(0, self.shape[0] * self.shape[1])
                    if not mine in mine_positions:
                        mine_positions.append(mine)
                        break
        
        for pos in mine_positions:
            self.write(pos, 9)
        
        print(self.array)
    def win(self):
        return True
    
    def read(self, position):
        return self.array[self.get_index(position)][self.get_position(position)]
    
    def write(self, position, new):
        self.array[self.get_index(position)][self.get_position(position)] = new

    def get_index(self, position):
        return math.floor(abcs.index(position[0]) / self.shape[1])
    
    def get_position(self, position):
        return math.floor(position[1] % self.shape[1])


field = Field()

start = time.time()
while True:
    while True:
        action = str(input("Set or Reveal? "))
        if action != "R" and action != "S":
            print("Invalid action.")
            continue
        break
    while True:
        f = str(input("Position? ")).lower()
        if not field.correct_format(f):
            print("Wrong format.")
            continue
        break
    
    if field.win():
        print("You won!")
        break

end = time.time()
print(str(datetime.timedelta(seconds = math.floor(end - start))))
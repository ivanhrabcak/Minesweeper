import time, random, math, datetime

#abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Input - x.z

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Field:
    def __init__(self, shape = [10, 10], mines = 10, array = []):
        self.shape = shape
        self.mines = mines
        if array == []:
            self.array = self.gen()
            self.fill_mines()
        else:
            self.array = array
    
    def gen(self):
        arr = []
        for i in range(self.shape[0]):
            l = []
            for i in range(self.shape[1]):
                l.append(0)
            arr.append(l)
        return arr
    
    def correct_format(self, position):
        correct = True
        if "." not in position:
            return False
        else:
            column = int(position.split(".")[0])
            row = int(position.split(".")[1])
            if column < self.shape[1] and row < self.shape[0]:
                return True
            else:
                return False
    
    def fill_mines(self):

        mine_positions = []
        for n in range(0, self.mines):
            mine = random.randint(0, self.shape[0] * self.shape[1])
            x = random.randomint(0, self.shape[0])
            y = random.randomint(0, self.shape[1])
            point = Point(x, y)
            if not mine in mine_positions:
                mine_positions.append(mine)
            else:
                while True:
                    mine = random.randint(0, self.shape[0] * self.shape[1])
                    if not mine in mine_positions:
                        mine_positions.append(mine)
                        break
            # while True:
            #         mine = random.randint(0, self.shape[0] * self.shape[1])
            #         if mine in mine_positions:
            #             break
                        
            #     mine_positions.append(mine)
        
        for pos in mine_positions:
            self.write(pos, pos.X, pos.Y)#[2][2]
        
        print(self.array)
    
    def win(self):
        return True
    
    def read(self, position):
        return self.array[self.get_index(position)][self.get_position(position)]
    
    def write(self, positiona, positionb, new):
        self.array[self.get_index(position)][self.get_position(position)] = new

    def get_index(self, position):
        return math.floor(position / self.shape[1])
    
    def get_position(self, position):
        return math.floor(position % self.shape[1])


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
    x = int(f.split(".")[0]
    y = int(f.split(".")[2]
    point = Point(x, y)
    field.write(point.X, point.Y), 99999999)
    if field.win():
        print("You won!")
        break

end = time.time()
print(str(datetime.timedelta(seconds = math.floor(end - start))))

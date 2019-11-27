import time, random, math, datetime, sys

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
        self.map = self.gen()
        self.turn = 1
    
    def gen(self):
        arr = []
        for i in range(self.shape[0] + 2):
            l = []
            for i in range(self.shape[1] + 2):
                l.append(0)
            arr.append(l)
        return arr
    
    def correct_format(self, position):
        if "." not in position:
            return False
        else:
            column = int(position.split(".")[0])
            row = int(position.split(".")[1])
            if column < self.shape[1] and row < self.shape[0]:
                return True
            else:
                return False
    
    def increment_field(self, px, py, by = 1):
        self.array[px][py] += by

    def fill_numbers(self, mine_positions):
        for mine in mine_positions:
            self.increment_field(mine.x, mine.y)

    def fill_mines(self):
        mine_positions = []
        while True:
            mine = Point(random.randint(0, self.shape[0] - 1), random.randint(0, self.shape[1] - 1))
            if len(mine_positions) == self.mines:
                break
            if mine in mine_positions:
                continue
            else:
                mine_positions.append(mine)
        
        for pos in mine_positions:
            self.increment_field(pos.x, pos.y, 9)#[2][2]
        self.fill_numbers(mine_positions)
    
    def win(self):
        return True
    
    def read(self, px, py):
        return self.array[px + 1][py + 1]
    
    def write(self, px, py, new):
        self.array[px + 1][py + 1] = new
    
    def reveal(self, posx, posy):
        p = Point(posx, posy)
    
    def set(self, posx, posy):
        self.map[posx][posy]

    def draw(self):
        number_line = 0
        print("- ", end = "")
        for i in range(self.shape[1]):
            print(i, end = " ")
        for r in range(self.shape[0]):
            print("")
            print(number_line, end = " ")
            number_line += 1
            r += 1
            for i in range(self.shape[1]):
                i += 1
                c = self.map[r][i]
                print(c, end = " ")

field = Field()

print(field.map)

field.draw()

start = time.time()
while True:
    while True:
        action = str(input("\nSet or Reveal? "))
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
    x = int(f.split(".")[0])
    y = int(f.split(".")[1])
    point = Point(x, y)
    
    field.draw()
    
    if action == "R":
        field.reveal(point.x, point.y)
    elif action == "S":
        field.set(point.x, point.y)
    
    
    if field.win():
        print("\nYou won!")
        break

end = time.time()
print(str(datetime.timedelta(seconds = math.floor(end - start))))

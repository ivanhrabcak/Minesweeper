import time, random, math, datetime, sys

# Input - x.z

## Map
# unrevealed: -1
# flag: -2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def eqalsTo(self, point2):
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False

class Field:
    def __init__(self, shape = [10, 10], mines = 10, array = []):
        self.shape = shape
        self.mines = mines
        if array == []:
            self.array = self.gen()
            self.fill_mines()
        else:
            self.array = array
        self.map = self.gen(n = -1)
        self.turn = 1
        self.flags = []
    
    def gen(self, n = 0):
        arr = []
        for i in range(self.shape[0] + 2):
            l = []
            for i in range(self.shape[1] + 2):
                l.append(n)
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

    def fill_numbers(self):
        for j in range(-1, 2):
            for i in range(-1, 2): 
                if j == 0 and i == 0:
                    continue
                
                for mine in self.mine_positions:
                    if self.array[i][j] == 9:
                        continue
                    self.increment_field(mine.x + i, mine.y + j)
    

    def fill_mines(self):
        self.mine_positions = []
        # while True:
        #     mine = Point(random.randint(0, self.shape[0] - 1), random.randint(0, self.shape[1] - 1))
        #     if len(self.mine_positions) == self.mines:
        #         break
        #     if mine in self.mine_positions:
        #         continue
        #     else:
        #         self.mine_positions.append(mine)
        self.mine_positions.append(Point(0,0))
        self.mine_positions.append(Point(1,1))
        self.mine_positions.append(Point(2,2))
        self.mine_positions.append(Point(4,4))
        
        for pos in self.mine_positions:
            self.increment_field(pos.x, pos.y, 9)#[2][2]

        self.fill_numbers()
    
    def win(self):
        for i in self.map:
            for a in i:
                if type(i) == str:
                    continue
                if a >= 9:
                    print(a)
                    return False
        correct = []
        for mine in self.flags:
            for i in self.mine_positions:
                if [i.x, i.y] == [mine.x, mine.y]:
                    correct.append(mine)
        if len(correct) == self.mines:
            return True
        else:
            return None
    
    def read(self, px, py):
        return self.array[px + 1][py + 1]
    
    def write(self, px, py, new):
        self.array[px + 1][py + 1] = new
 
    def isInBounds(self, pos):
        return pos.x > 0 and pos.x <= 9 and pos.y > 0 and pos.y <= 9

    def reveal(self, posx, posy, recursion = False):
        for i in range(-1, 1):
            if i == 0:
                continue
            if self.isInBounds(Point(posx, posy)):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if self.array[posx][posy] < 9 and self.array[posx][posy] != self.map[posx][posy]:
                            self.map[posx][posy] = self.array[posx][posy]
                            self.reveal(posx + i, posy + j, True)
                        elif self.array[posx][posy] == 9 and not recursion:
                            self.map[posx][posy] = self.array[posx][posy]
                            return
                        elif self.array[posx][posy] < 9 and not recursion:
                            self.reveal(posx + i, posy + j, True)
                        else:
                            return
                            


                # #if self.array[posx][posy] == self.map[posx][posy]
                # if self.array[posx][posy] < 9:
                #     self.map[posx][posy] = self.array[posx][posy]
                #     self.reveal(posx + i, posy, True)
                #     self.reveal(posx, posy + i, True)
                #     self.reveal(posx + i, posy + i, True)
                # elif self.array[posx][posy] == 9 and not recursion:
                #     self.map[posx][posy] = self.array[posx][posy]
                #     return
    
    def setField(self, point): 
        elif self.array[point.x + 1][point.y + 1] !=
        elif [point.x, point.y] not in self.flags:
            self.map[point.x + 1][point.y + 1] = -2
            print(self.map)
            self.flags.append(point)
            print("Flag set!\n")
        else:
            print("There's already a flag there. ")

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
                field = self.map[r][i] 
                if field >= 0:
                    c = field
                elif self.map[r][i] == -1:
                    c = 0
                elif self.map[r][i] == -2:
                    c = "F"
                elif self.map[r][i] == 9:
                    c = "M"
                print(c, end = " ")
                
# f = [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

field = Field(shape = [10, 10], mines = 10)

field.draw()

start = time.time()
while True:
    while True:
        action = str(input("\nSet or Reveal? ")).lower()
        if action != "r" and action != "s":
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
    if action == "r":
        field.reveal(point.x, point.y)
    elif action == "s":
        field.setField(point)
    won = field.win()
    if won:
        print("")
        field.draw()
        print("\nYou won!")
        break
    elif won == None:
        field.draw()
        pass
    else:
        print("")
        field.draw()
        print("\nYou lost!")
        break
    
end = time.time()
print(str(datetime.timedelta(seconds = math.floor(end - start))))
